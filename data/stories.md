## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## answer_fees
* ask_fees
  - slot{"admin_feature":"fee structure"}
  - utter_ask_course
* choose{"course": "BCA"}
  - slot{"course": "BCA"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_fees1
* ask_fees
  - slot{"admin_feature":"fee structure"}
  - utter_ask_course
* choose{"course": "BBA-IT"}
  <!-- - course_form
  - form{"name":"course_form"} -->
  - slot{"course": "BBA-IT"}
  <!-- - form{"name":"null"} -->
  - action_admin_feature
  - utter_did_that_help
* deny
  - utter_ask
* affirm
  - utter_happy

## answer_fees2
* ask_fees
  - slot{"admin_feature":"fee structure"}
  - utter_ask_course
* choose{"course": "MSC-CA"}
  <!-- - course_form
  - form{"name":"course_form"} -->
  - slot{"course": "MSC-CA"}
  <!-- - form{"name":"null"} -->
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

<!-- ## answer_fees3
* ask_fees{"course": "BCA"}
  <!-- - course_form
  - form{"name":"course_form"} -->
  <!-- - slot{"admin_feature":"fee structure"}
  - slot{"course": "BCA"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye -->

## answer_eligibility
* ask_eligibility
  - slot{"admin_feature":"eligibility criteria"}
  - utter_ask_course
* choose{"course": "BCA"}
  - slot{"course": "BCA"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_eligibility1
* ask_eligibility
  - slot{"admin_feature":"eligibility criteria"}
  - utter_ask_course
* choose{"course": "MBA-IT"}
  - slot{"course": "MBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* deny
  - utter_ask
* affirm
  - utter_happy

<!-- ## answer_eligibility3
* ask_eligibility{"course": "BBA-IT"}
  - slot{"admin_feature":"eligibility criteria"}
  - slot{"course": "BBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye -->

## answer_selection
* ask_selection
  - slot{"admin_feature":"selection procedure"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask

## answer_selection1
* ask_selection
  - slot{"admin_feature":"selection procedure"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_happy

<!-- ## answer_selection2
* ask_selection{"course":"MSC-SS"}
  - slot{"admin_feature":"selection procedure"}
  - slot{"course":"MSC-SS"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye -->

## answer_application
* ask_application
  - slot{"admin_feature":"how to apply"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* deny
  - utter_ask
* deny
  - utter_goodbye

## answer_application1
* ask_application
  - slot{"admin_feature":"how to apply"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

<!-- ## answer_application2
* ask_application{"course":"BCA"}
  - slot{"admin_feature":"how to apply"}
  - slot{"course":"BCA"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy -->

## answer_rules
* ask_rules
  - slot{"admin_feature":"rules"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* deny
  - utter_ask
* deny
  - utter_goodbye

## answer_rules1
* ask_rules
  - slot{"admin_feature":"rules"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

<!-- ## answer_rules2
* ask_rules{"course":"BCA"}
  - slot{"admin_feature":"rules"}
  - slot{"course":"BCA"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy -->

## answer_dates
* ask_dates
  - slot{"admin_feature":"important dates"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* deny
  - utter_ask
* deny
  - utter_goodbye

## answer_dates1
* ask_dates
  - slot{"admin_feature":"important dates"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

<!-- ## answer_dates2
* ask_dates{"course":"BCA"}
  - slot{"admin_feature":"important dates"}
  - slot{"course":"BCA"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy -->

## answer_curriculum
* ask_curriculum
  - slot{"course_feature":"curriculum"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_course_feature
  - utter_did_that_help
* deny
  - utter_ask
* deny
  - utter_goodbye

## answer_curriculum1
* ask_curriculum
  - slot{"course_feature":"curriculum"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

<!-- ## answer_curriculum2
* ask_curriculum{"course":"BCA"}
  - slot{"course_feature":"curriculum"}
  - slot{"course":"BCA"}
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy -->

## answer_syllabus
* ask_syllabus
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_course_feature
  - utter_did_that_help
* deny
  - utter_ask
* deny
  - utter_goodbye

## answer_syllabus1
* ask_syllabus
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

<!-- ## answer_syllabus2
* ask_syllabus{"course":"BCA"}
  - slot{"course_feature":"syllabus"}
  - slot{"course":"BCA"}
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy -->

## answer_objectives
* ask_objectives
  - slot{"course_feature":"objectives"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_course_feature
  - utter_did_that_help
* deny
  - utter_ask
* deny
  - utter_goodbye

## answer_objectives1
* ask_objectives
  - slot{"course_feature":"objectives"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

<!-- ## answer_objectives2
* ask_objectives{"course":"BCA"}
  - slot{"course_feature":"objectives"}
  - slot{"course":"BCA"}
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy -->

## answer_outcomes
* ask_outcomes
  - slot{"course_feature":"outcomes"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_course_feature
  - utter_did_that_help
* deny
  - utter_ask
* deny
  - utter_goodbye

## answer_outcomes1
* ask_outcomes
  - slot{"course_feature":"outcomes"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_courses
* ask_courses
  - utter_course
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_courses1
* ask_courses
  - utter_course
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy
  
<!-- ## answer_outcomes2
* ask_outcomes{"course":"BCA"}
  - slot{"course_feature":"outcomes"}
  - slot{"course":"BCA"}
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy -->

<!-- ## answer_select&eligibility
* ask_selection+ask_eligibility
  - slot{"admin_feature":"eligibility criteria"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_select&eligibility1
* ask_selection+ask_eligibility
  - slot{"admin_feature":"eligibility criteria"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_select&eligibility2
* ask_selection+ask_eligibility{"course":"BBA-IT"}
  - slot{"admin_feature":"eligibility criteria"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_apply&select2
* ask_application+ask_selection
  - slot{"admin_feature":"selection"}
  - utter_ask_course
* choose{"course":"BCA"}
  - slot{"course":"BCA"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_apply&select
* ask_application+ask_selection{"course":"BBA-IT"}
  - slot{"admin_feature":"selection"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_apply&select1
* ask_application+ask_selection
  - slot{"admin_feature":"selection"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_admin_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_fees&syllabus
* ask_fees+ask_syllabus
  - slot{"admin_feature":"fees structure"}
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"BCA"}
  - slot{"course":"BCA"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_fees&syllabus1
* ask_fees+ask_syllabus
  - slot{"admin_feature":"fees structure"}
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_fees&syllabus2
* ask_fees+ask_syllabus{"course":"BCA"}
  - slot{"admin_feature":"fees structure"}
  - slot{"course_feature":"syllabus"}
  - slot{"course":"BCA"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_select&syllabus
* ask_fees+ask_syllabus
  - slot{"admin_feature":"selection procedure"}
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"BCA"}
  - slot{"course":"BCA"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_select&syllabus1
* ask_fees+ask_syllabus
  - slot{"admin_feature":"fees structure"}
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_select&syllabus2
* ask_fees+ask_syllabus{"course":"BCA"}
  - slot{"admin_feature":"fees structure"}
  - slot{"course_feature":"syllabus"}
  - slot{"course":"BCA"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_apply&syllabus
* ask_application+ask_syllabus
  - slot{"admin_feature":"how to apply"}
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_apply&syllabus1
* ask_application+ask_syllabus
  - slot{"admin_feature":"how to apply"}
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"MBA-IT"}
  - slot{"course":"MBA-IT"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_apply&syllabus2
* ask_application+ask_syllabus{"course":"MSC-SS"}
  - slot{"admin_feature":"how to apply"}
  - slot{"course_feature":"syllabus"}
  - slot{"course":"MSC-SS"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_eligibility&syllabus
* ask_eligibility+ask_syllabus
  - slot{"admin_feature":"eligibility criteria"}
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"BBA-IT"}
  - slot{"course":"BBA-IT"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* affirm
  - utter_happy

## answer_eligibility&syllabus1
* ask_eligibility+ask_syllabus
  - slot{"admin_feature":"eligibility criteria"}
  - slot{"course_feature":"syllabus"}
  - utter_ask_course
* choose{"course":"BCA"}
  - slot{"course":"BCA"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye

## answer_eligibility&syllabus2
* ask_eligibility+ask_syllabus{"course":"MSC-CA"}
  - slot{"admin_feature":"eligibility criteria"}
  - slot{"course_feature":"syllabus"}
  - slot{"course":"MSC-CA"}
  - action_admin_feature
  - action_course_feature
  - utter_did_that_help
* affirm
  - utter_ask
* deny
  - utter_goodbye -->
