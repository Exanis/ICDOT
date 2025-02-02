DEFAULT = (
    (
        None,
        {
            "fields": ("transplant_date", "donor_ref", "recipient_ref"),
        },
    ),
    (
        "Recipient",
        {
            "classes": ("collapse",),
            "fields": (
                "recipient_record_date",
                "recipient_dob",
                ("recipient_height", "recipient_height_units"),
                ("recipient_weight", "recipient_weight_units"),
                "recipient_sex",
                "recipient_ethnicity",
                ("pre_transplant_dialysis", "time_on_dialysis"),
                "previous_transplant",
                "primary_kidney_disease",
                "recipient_cmv_status",
                "recipient_ebv_status",
                (
                    "recipient_hbv_ag_status",
                    "recipient_hbv_as_status",
                    "recipient_hbv_ac_status",
                ),
                "recipient_hcv_status",
                "recipient_hiv_status",
            ),
        },
    ),
    (
        "Outcomes/events",
        {
            "classes": ("collapse",),
            "fields": (
                "recipient_death_date",
                "graft_failure_date",
                "graft_failure_cause",
            ),
        },
    ),
    (
        "Donor",
        {
            "classes": ("collapse",),
            "fields": (
                "donor_record_date",
                ("donor_dob", "donor_age"),
                "donor_sex",
                "donor_ethnicity",
                "donor_criteria",
                "donor_type",
                "living_donor_type",
                ("deceased_donor_type", "donor_death_cause"),
                "kdri",
                "donor_diabetes",
                "donor_hypertension",
                "donor_comorbities",
                "donor_egfr",
                ("donor_proteinuria", "donor_proteinuria_units"),
                ("donor_proteinuria_dipstick", "donor_proteinuria_dipstick_units"),
                ("donor_creatinemia", "donor_creatinemia_units"),
            ),
        },
    ),
    (
        "Graft",
        {
            "classes": ("collapse",),
            "fields": (
                "procurement_date",
                "donor_aboi",
                ("hla_a_mismatches", "hla_b_mismatches", "hla_dr_mismatches"),
                ("cold_ischemia_time", "cold_ischemia_time_units"),
                ("delayed_graft_function", "dgf_time", "dgf_time_units"),
                "induction_therapy",
                "preformed_dsa",
                "dsa_date",
                "immunodominant_dsa_class",
                "i_dsa_specificity",
                "i_dsa_mfi",
                "c1q_binding",
            ),
        },
    ),
    (
        "Day 0 biopsy",
        {
            "classes": ("collapse",),
            "fields": (
                "pre_transplant_biopsy_type",
                "ci_score",
                "ct_score",
                "cv_score",
                "ah_score",
                "percent_glomerulosclerosis",
            ),
        },
    ),
)
