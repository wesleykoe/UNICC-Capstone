# test_evaluate_system.py
# ============================================================
# Unit and integration tests for evaluate_system.py
# Run with: pytest test_evaluate_system.py -v
# ============================================================

import json
import pytest
import sys
import os

# Allow import without GPU
os.environ["CUDA_VISIBLE_DEVICES"] = ""
sys.path.insert(0, os.path.dirname(__file__))


# ============================================================
# UNIT TESTS — clean_raw_output()
# ============================================================

from evaluate_system import clean_raw_output, extract_json, normalize_expert_output, arbitrate

class TestCleanRawOutput:

    def test_fixes_double_quotes(self):
        raw    = '{"key1""key2": "value"}'
        result = clean_raw_output(raw)
        assert '""' not in result

    def test_removes_trailing_comma_before_brace(self):
        raw    = '{"key": "value",}'
        result = clean_raw_output(raw)
        assert ',}' not in result

    def test_removes_trailing_comma_before_bracket(self):
        raw    = '["a", "b",]'
        result = clean_raw_output(raw)
        assert ',]' not in result

    def test_removes_period_after_quote(self):
        raw    = '{"key": "value".}'
        result = clean_raw_output(raw)
        assert '".' not in result

    def test_fixes_semicolons(self):
        raw    = '{"key": "hello; world"}'
        result = clean_raw_output(raw)
        assert result is not None


# ============================================================
# UNIT TESTS — extract_json()
# ============================================================

class TestExtractJson:

    def test_extracts_valid_json(self):
        raw    = '{"expert_name": "Governance Expert", "overall_status": "Fail"}'
        result = extract_json(raw)
        assert result is not None
        assert result['expert_name'] == 'Governance Expert'
        assert result['overall_status'] == 'Fail'

    def test_returns_none_for_empty_string(self):
        assert extract_json('') is None

    def test_returns_none_for_no_json(self):
        assert extract_json('This is just plain text with no JSON') is None

    def test_extracts_json_with_trailing_text(self):
        raw    = '{"key": "value"} some extra text after'
        result = extract_json(raw)
        assert result is not None
        assert result['key'] == 'value'

    def test_extracts_json_with_leading_text(self):
        raw    = 'Some preamble text\n{"key": "value"}'
        result = extract_json(raw)
        assert result is not None
        assert result['key'] == 'value'

    def test_handles_missing_comma_between_fields(self):
        raw    = '{"field1": "value1"\n"field2": "value2"}'
        result = extract_json(raw)
        assert result is not None

    def test_handles_trailing_comma(self):
        raw    = '{"field1": "value1", "field2": "value2",}'
        result = extract_json(raw)
        assert result is not None

    def test_handles_truncated_json(self):
        # Model cut off mid-output
        raw    = '{"expert_name": "Threat Expert", "overall_status": "Fail"'
        result = extract_json(raw)
        # Should either parse or return None gracefully — never raise
        assert result is None or isinstance(result, dict)

    def test_handles_framework_references_array(self):
        raw = json.dumps({
            "expert_name": "Governance Expert",
            "overall_status": "Pass",
            "risk_level": "Low",
            "recommended_action": "Approve",
            "requires_human_review": False,
            "confidence_level": "High",
            "rationale_summary": "No issues detected.",
            "framework_references": ["UN AI Ethics Guidelines", "GDPR Article 22"]
        })
        result = extract_json(raw)
        assert result is not None
        assert isinstance(result['framework_references'], list)
        assert len(result['framework_references']) == 2


# ============================================================
# UNIT TESTS — normalize_expert_output()
# ============================================================

class TestNormalizeExpertOutput:

    def test_fixes_string_placeholder_name(self):
        parsed = {"expert_name": "string", "overall_status": "Pass",
                  "risk_level": "Low", "recommended_action": "Approve",
                  "requires_human_review": False, "confidence_level": "High",
                  "rationale_summary": "OK", "framework_references": []}
        result = normalize_expert_output(parsed, "Governance Expert")
        assert result['expert_name'] == 'Governance Expert'

    def test_fixes_empty_name(self):
        parsed = {"expert_name": "", "overall_status": "Pass",
                  "risk_level": "Low", "recommended_action": "Approve",
                  "requires_human_review": False, "confidence_level": "High",
                  "rationale_summary": "OK", "framework_references": []}
        result = normalize_expert_output(parsed, "Threat Expert")
        assert result['expert_name'] == 'Threat Expert'

    def test_defaults_invalid_status(self):
        parsed = {"expert_name": "Governance Expert", "overall_status": "Unknown",
                  "risk_level": "Low", "recommended_action": "Approve",
                  "requires_human_review": False, "confidence_level": "High",
                  "rationale_summary": "OK", "framework_references": []}
        result = normalize_expert_output(parsed, "Governance Expert")
        assert result['overall_status'] == 'Caution'

    def test_defaults_invalid_risk(self):
        parsed = {"expert_name": "Governance Expert", "overall_status": "Pass",
                  "risk_level": "Extreme", "recommended_action": "Approve",
                  "requires_human_review": False, "confidence_level": "High",
                  "rationale_summary": "OK", "framework_references": []}
        result = normalize_expert_output(parsed, "Governance Expert")
        assert result['risk_level'] == 'Moderate'

    def test_defaults_invalid_action(self):
        parsed = {"expert_name": "Governance Expert", "overall_status": "Pass",
                  "risk_level": "Low", "recommended_action": "Destroy",
                  "requires_human_review": False, "confidence_level": "High",
                  "rationale_summary": "OK", "framework_references": []}
        result = normalize_expert_output(parsed, "Governance Expert")
        assert result['recommended_action'] == 'Escalate'

    def test_converts_singular_framework_reference(self):
        parsed = {"expert_name": "Threat Expert", "overall_status": "Fail",
                  "risk_level": "High", "recommended_action": "Escalate",
                  "requires_human_review": True, "confidence_level": "High",
                  "rationale_summary": "Risk found.", "framework_reference": "NIST CSF 2.0"}
        result = normalize_expert_output(parsed, "Threat Expert")
        assert 'framework_references' in result
        assert isinstance(result['framework_references'], list)
        assert result['framework_references'][0] == 'NIST CSF 2.0'

    def test_ensures_framework_references_is_list(self):
        parsed = {"expert_name": "Behavioral Expert", "overall_status": "Pass",
                  "risk_level": "Low", "recommended_action": "Approve",
                  "requires_human_review": False, "confidence_level": "High",
                  "rationale_summary": "OK", "framework_references": "IEEE Ethically Aligned Design"}
        result = normalize_expert_output(parsed, "Behavioral Expert")
        assert isinstance(result['framework_references'], list)

    def test_requires_human_review_is_boolean(self):
        parsed = {"expert_name": "Governance Expert", "overall_status": "Pass",
                  "risk_level": "Low", "recommended_action": "Approve",
                  "requires_human_review": "yes", "confidence_level": "High",
                  "rationale_summary": "OK", "framework_references": []}
        result = normalize_expert_output(parsed, "Governance Expert")
        assert isinstance(result['requires_human_review'], bool)


# ============================================================
# UNIT TESTS — arbitrate()
# ============================================================

class TestArbitrate:

    def _make_expert(self, name, status, risk, action, review=True, conf="High", rationale="OK"):
        return {
            "expert_name": name, "overall_status": status,
            "risk_level": risk, "recommended_action": action,
            "requires_human_review": review, "confidence_level": conf,
            "rationale_summary": rationale, "framework_references": []
        }

    def test_rule_1_any_reject_triggers_reject(self):
        gov = self._make_expert("Governance Expert", "Fail", "High", "Escalate")
        thr = self._make_expert("Threat Expert",     "Fail", "High", "Escalate")
        beh = self._make_expert("Behavioral Expert", "Fail", "High", "Reject")
        result = arbitrate(gov, thr, beh)
        assert result['final_decision'] == 'Reject'

    def test_rule_2_any_escalate_triggers_escalate(self):
        gov = self._make_expert("Governance Expert", "Caution", "Moderate", "Escalate")
        thr = self._make_expert("Threat Expert",     "Pass",    "Low",      "Approve")
        beh = self._make_expert("Behavioral Expert", "Pass",    "Low",      "Approve")
        result = arbitrate(gov, thr, beh)
        assert result['final_decision'] == 'Escalate'

    def test_rule_3_any_fail_triggers_escalate(self):
        gov = self._make_expert("Governance Expert", "Fail",  "High", "Revise")
        thr = self._make_expert("Threat Expert",     "Pass",  "Low",  "Approve")
        beh = self._make_expert("Behavioral Expert", "Pass",  "Low",  "Approve")
        result = arbitrate(gov, thr, beh)
        assert result['final_decision'] == 'Escalate'

    def test_rule_4_any_revise_triggers_revise(self):
        gov = self._make_expert("Governance Expert", "Caution", "Moderate", "Revise")
        thr = self._make_expert("Threat Expert",     "Pass",    "Low",      "Approve")
        beh = self._make_expert("Behavioral Expert", "Pass",    "Low",      "Approve")
        result = arbitrate(gov, thr, beh)
        assert result['final_decision'] == 'Revise'

    def test_rule_5_any_caution_triggers_revise(self):
        gov = self._make_expert("Governance Expert", "Caution", "Moderate", "Approve")
        thr = self._make_expert("Threat Expert",     "Pass",    "Low",      "Approve")
        beh = self._make_expert("Behavioral Expert", "Pass",    "Low",      "Approve")
        result = arbitrate(gov, thr, beh)
        assert result['final_decision'] == 'Revise'

    def test_rule_6_all_pass_triggers_approve(self):
        gov = self._make_expert("Governance Expert", "Pass", "Low", "Approve", review=False, conf="High")
        thr = self._make_expert("Threat Expert",     "Pass", "Low", "Approve", review=False, conf="High")
        beh = self._make_expert("Behavioral Expert", "Pass", "Low", "Approve", review=False, conf="High")
        result = arbitrate(gov, thr, beh)
        assert result['final_decision'] == 'Approve'

    def test_reject_takes_priority_over_escalate(self):
        gov = self._make_expert("Governance Expert", "Fail", "Critical", "Reject")
        thr = self._make_expert("Threat Expert",     "Fail", "High",     "Escalate")
        beh = self._make_expert("Behavioral Expert", "Fail", "High",     "Escalate")
        result = arbitrate(gov, thr, beh)
        assert result['final_decision'] == 'Reject'

    def test_final_risk_is_maximum(self):
        gov = self._make_expert("Governance Expert", "Fail", "Critical", "Reject")
        thr = self._make_expert("Threat Expert",     "Fail", "High",     "Escalate")
        beh = self._make_expert("Behavioral Expert", "Pass", "Low",      "Approve")
        result = arbitrate(gov, thr, beh)
        assert result['final_risk_level'] == 'Critical'

    def test_human_review_true_if_any_requires_it(self):
        gov = self._make_expert("Governance Expert", "Pass", "Low", "Approve", review=True)
        thr = self._make_expert("Threat Expert",     "Pass", "Low", "Approve", review=False)
        beh = self._make_expert("Behavioral Expert", "Pass", "Low", "Approve", review=False)
        result = arbitrate(gov, thr, beh)
        assert result['human_review_required'] is True

    def test_human_review_false_if_none_require_it(self):
        gov = self._make_expert("Governance Expert", "Pass", "Low", "Approve", review=False, conf="High")
        thr = self._make_expert("Threat Expert",     "Pass", "Low", "Approve", review=False, conf="High")
        beh = self._make_expert("Behavioral Expert", "Pass", "Low", "Approve", review=False, conf="High")
        result = arbitrate(gov, thr, beh)
        assert result['human_review_required'] is False

    def test_confidence_is_minimum(self):
        gov = self._make_expert("Governance Expert", "Fail", "High", "Escalate", conf="High")
        thr = self._make_expert("Threat Expert",     "Fail", "High", "Escalate", conf="Low")
        beh = self._make_expert("Behavioral Expert", "Fail", "High", "Escalate", conf="Moderate")
        result = arbitrate(gov, thr, beh)
        assert result['confidence_level'] == 'Low'

    def test_full_agreement_consensus(self):
        gov = self._make_expert("Governance Expert", "Fail", "High", "Escalate")
        thr = self._make_expert("Threat Expert",     "Fail", "High", "Escalate")
        beh = self._make_expert("Behavioral Expert", "Fail", "High", "Escalate")
        result = arbitrate(gov, thr, beh)
        assert result['consensus_level'] == 'Full Agreement'

    def test_majority_agreement_consensus(self):
        gov = self._make_expert("Governance Expert", "Fail", "High", "Escalate")
        thr = self._make_expert("Threat Expert",     "Fail", "High", "Escalate")
        beh = self._make_expert("Behavioral Expert", "Fail", "High", "Reject")
        result = arbitrate(gov, thr, beh)
        assert result['consensus_level'] == 'Majority Agreement'

    def test_structured_disagreement_consensus(self):
        gov = self._make_expert("Governance Expert", "Fail",    "High",     "Escalate")
        thr = self._make_expert("Threat Expert",     "Caution", "Moderate", "Revise")
        beh = self._make_expert("Behavioral Expert", "Fail",    "High",     "Reject")
        result = arbitrate(gov, thr, beh)
        assert result['consensus_level'] == 'Structured Disagreement'

    def test_output_contains_all_required_fields(self):
        gov = self._make_expert("Governance Expert", "Fail", "High", "Escalate")
        thr = self._make_expert("Threat Expert",     "Fail", "High", "Escalate")
        beh = self._make_expert("Behavioral Expert", "Fail", "High", "Escalate")
        result = arbitrate(gov, thr, beh)
        required_fields = [
            'final_decision', 'final_risk_level', 'consensus_level',
            'summary_of_key_disagreements', 'dominant_expert_influence',
            'human_review_required', 'conditions_for_approval',
            'mitigation_requirements', 'confidence_level',
            'final_rationale', 'cited_frameworks'
        ]
        for field in required_fields:
            assert field in result, f"Missing field: {field}"
