## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- hola
- howdy
- good morning
- good evening
- good afternoon

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- thank you
- talk to you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- okay

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

##intent:choose
- [BCA](course)
- [BBA-IT](course)
- [MSC-CA](course)
- [MSC-SS](course)
- [MSC-CA](course)
- [MBA-IT](course)

##intent:feature
- [fee structure](admin_feature)
- [eligibility criteria](admin_feature)
- [selection procedure](admin_feature)
- [how to apply](admin_feature)
- [rules](admin_feature)
- [important dates](admin_feature)
<!-- - [UG admissions](admissions)
- [MSC admissions](admissions)
- [MBA-IT admissions](admissions) -->
- [curriculum](course_feature)
- [objectives](course_feature)
- [syllabus](course_feature)
- [program outcomes](course_feature)

## intent:ask_courses
- what are the courses offered at SICSR?
- i want to know the courses taught at this college
- what are the courses taught
- i want to know the courses offered

## intent:ask_fees
- what is the [fees structure]{"entity":"admin_feature","value":"fee structure"}?
- what is the [payment structure]{"entity":"admin_feature", "value":"fee structure"}?
- what is the [cost]{"entity":"admin_feature", "value":"fee structure"} for this course?
- what is the annual [amount of money]{"entity":"admin_feature", "value":"fee structure"} spent on this course?
- [fees structure]{"entity":"admin_feature","value":"fee structure"} of [bca]{"entity":"course", "value":"BCA"}
- [payment structure]{"entity":"admin_feature", "value":"fee structure"} of [BCA]{"entity":"course"}
- [cost]{"entity":"admin_feature", "value":"fee structure"} of [bachelor in computer applications]{"entity":"course", "value":"BCA"}
- [fees structure]{"entity":"admin_feature"} for [bba]{"entity":"course", "value":"BBA-IT"}
- [payment structure]{"entity":"admin_feature", "value":"fee structure"} for [BBA-IT]{"entity":"course"}
- [cost]{"entity":"admin_feature", "value":"fee structure"} of [bachelor in business administration]{"entity":"course", "value":"BBA-IT"}
- [fees structure]{"entity":"admin_feature", "value":"fee structure"} for [msc-ca]{"entity":"course", "value":"MSC-CA"}
- [payment structure]{"entity":"admin_feature", "value":"fee structure"} for [MSC-CA]{"entity":"course"}
- [cost]{"entity":"admin_feature", "value":"fee structure"} of [masters of science in computer applications]{"entity":"course", "value":"MSC-CA"}
- [fees structure]{"entity":"admin_feature", "value":"fee structure"} for [msc-ss]{"entity":"course", "value":"MSC-SS"}
- [payment structure]{"entity":"admin_feature", "value":"fee structure"} for [MSC-SS]{"entity":"course"}
- [cost]{"entity":"admin_feature", "value":"fee structure"} of [masters of science in system security]{"entity":"course", "value":"MSC-SS"}
- [fees structure]{"entity":"admin_feature", "value":"fee structure"} for [mba-it]{"entity":"course", "value":"MBA-IT"}
- [payment structure]{"entity":"admin_feature", "value":"fee structure"} of [MBA-IT]{"entity":"course"}
- [cost]{"entity":"admin_feature", "value":"fee structure"} of [masters in business administration in IT]{"entity":"course", "value":"MBA-IT"}
<!-- - [fees structure]{"entity":"admin_feature", "value":"fee structure"} for [UG]{"entity":"admissions", "value":"UG admissions"}
- [payment structure]{"entity":"admin_feature", "value":"fee structure"} for [MSC]{"entity":"admissions", "value":"MSC admissions"}
- [cost]{"entity":"admin_feature", "value":"fee structure"} of [masters in science]{"entity":"admissions", "value":"MSC admissions"}
- [fees structure]{"entity":"admin_feature", "value":"fee structure"} for [under graduate]{"entity":"admissions", "value":"UG admissions"}
- [payment structure]{"entity":"admin_feature", "value":"fee structure"} for [bachelors]{"entity":"admissions", "value":"UG admissions"}
- [cost]{"entity":"admin_feature", "value":"fee structure"} of [masters]{"entity":"admissions", "value":"MSC admissions"}
- [cost]{"entity":"admin_feature", "value":"fee structure"} of [post graduate]{"entity":"admissions", "value":"MSC admissions"} -->

##intent:ask_eligibility
- what is the [eligibility criteria]{"entity":"admin_feature", "value":"eligibility criteria"} ?
- what is the [selection criteria]{"entity":"admin_feature", "value":"eligibility criteria"} ?
- [eligibility criteria]{"entity":"admin_feature"} for [BCA]{"entity":"course"}
- [selection criteria]{"entity":"admin_feature", "value":"eligibility criteria"} of [bachelor in computer applications]{"entity":"course", "value":"BCA"}
- [eligibility criteria]{"entity":"admin_feature"} for [bba]{"entity":"course", "value":"BBA-IT"}
- [selection criteria]{"entity":"admin_feature", "value":"eligibility criteria"} for [BBA]{"entity":"course", "value":"BBA-IT"}
<!-- - [eligibility criteria]{"entity":"admin_feature"} for [bachelors]{"entity":"admissions", "value":"UG admissions"} -->
- [selection criteria]{"entity":"admin_feature", "value":"eligibility criteria"} for [msc-ca]{"entity":"course", "value":"MSC-CA"}
- [eligibility criteria]{"entity":"admin_feature"} for [masters in business administration]{"entity":"course", "value":"MBA-IT"}
- [selection criteria]{"entity":"admin_feature", "value":"eligibility criteria"} for [MSC-SS]{"entity":"course", "value":"MSC-SS"}

##intent:ask_selection
- what is the [selection procedure]{"entity":"admin_feature", "value":"selection procedure"}?
- what is the [selection process]{"entity":"admin_feature", "value":"selection procedure"} of [bca]{"entity":"course", "value":"BCA"}?
- what is the [selection procedure]{"entity":"admin_feature", "value":"selection procedure"} for [bba]{"entity":"course", "value":"BBA-IT"}?
- what is the [selection process]{"entity":"admin_feature", "value":"selection procedure"} for [msc-ca]{"entity":"course", "value":"MSC-CA"}?
- what is the [selection procedure]{"entity":"admin_feature", "value":"selection procedure"} of [msc-ss]{"entity":"course", "value":"MSC-SS"}?
- what is the [selection procedure]{"entity":"admin_feature", "value":"selection procedure"} for [mba]{"entity":"course", "value":"MBA-IT"}?

##intent:ask_application
- i want to know how to [apply]{"entity":"admin_feature", "value":"how to apply"}
- i want to know the [application process]{"entity":"admin_feature", "value":"how to apply"} for [bba-it]{"entity":"course", "value":"BBA-IT"}
- i want to know the [application process]{"entity":"admin_feature", "value":"how to apply"} for [mba-it]{"entity":"course", "value":"MBA-IT"}
- i want to know the [application process]{"entity":"admin_feature", "value":"how to apply"} of [bca]{"entity":"course", "value":"BCA"}
- i want to know the [application process]{"entity":"admin_feature", "value":"how to apply"} for [msc-ca]{"entity":"course", "value":"MSC-CA"}
- i want to know the [application process]{"entity":"admin_feature", "value":"how to apply"} of [msc-ss]{"entity":"course", "value":"MSC-SS"}

##intent:ask_rules
- What are the rules and [regulations]{"entity":"admin_feature", "value":"rules"} of the institution?
- what are the [prohibited]{"entity":"admin_feature","value":"rules"} things in the college?
- what are the [prohibited]{"entity":"admin_feature","value":"rules"} things for [mba]{"entity":"course","value":"MBA-IT"}?
- What are the rules and [regulations]{"entity":"admin_feature", "value":"rules"} of the institution of [mba]{"entity":"course","value":"MBA-IT"}?
- What are the rules and [regulations]{"entity":"admin_feature", "value":"rules"} of the institution for [bba]{"entity":"course","value":"BBA-IT"}?
- What are the rules and [regulations]{"entity":"admin_feature", "value":"rules"} of the institution for [bca]{"entity":"course","value":"BCA"}?
- What are the rules and [regulations]{"entity":"admin_feature", "value":"rules"} of the institution of [msc-ca]{"entity":"course","value":"MSC-CA"}?
- What are the rules and [regulations]{"entity":"admin_feature", "value":"rules"} of the institution for [msc-ss]{"entity":"course","value":"MSC-SS"}?

##intent:ask_dates
- what are the [important dates]{"entity":"admin_feature","value":"important dates"} for the admission process for this college?
- what are the notable [events]{"entity":"admin_feature","value":"important dates"}?
- what are the notable [events]{"entity":"admin_feature","value":"important dates"} of admission in [msc-ca]{"entity":"course","value":"MSC-CA"}?
- what are the notable [events]{"entity":"admin_feature","value":"important dates"} for admission in [msc-ss]{"entity":"course","value":"MSC-SS"}?
- what are the notable [events]{"entity":"admin_feature","value":"important dates"} for admission in [mba-it]{"entity":"course","value":"MBA-IT"}?
- what are the notable [events]{"entity":"admin_feature","value":"important dates"} of admission in [bba-it]{"entity":"course","value":"BBA-IT"}?
- what are the notable [events]{"entity":"admin_feature","value":"important dates"} for admission in [bca]{"entity":"course","value":"BCA"}?

##intent:ask_curriculum
- I want to know the program [curriculum]{"entity":"course_feature", "value":"curriculum"}
- i want to know the [program structure]{"entity":"course_feature", "value":"curriculum"}
- i want to know the [course structure]{"entity":"course_feature", "value":"curriculum"}
- i want to know the [program structure]{"entity":"course_feature", "value":"curriculum"} of [bca]{"entity":"course", "value":"BCA"}
- I want to know the program [curriculum]{"entity":"course_feature", "value":"curriculum"} for [bba]{"entity":"course", "value":"BBA-IT"}
- I want to know the [course structure]{"entity":"course_feature", "value":"curriculum"} of [msc-ca]{"entity":"course", "value":"MSC-CA"}
- I want to know the program [curriculum]{"entity":"course_feature", "value":"curriculum"} for [msc-ss]{"entity":"course", "value":"MSC-SS"}
- I want to know the [course structure]{"entity":"course_feature", "value":"curriculum"} for [mba-it]{"entity":"course", "value":"MBA-IT"}

##intent:ask_syllabus
- I want to know the [syllabus]{"entity":"course_feature", "value":"syllabus"}
- I want to know the [syllabus]{"entity":"course_feature", "value":"syllabus"} for [bba]{"entity":"course", "value":"BBA-IT"}
- what are the [subjects]{"entity":"course_feature", "value":"syllabus"} in [bca]{"entity":"course", "value":"BCA"}
- I want to know the [syllabus]{"entity":"course_feature", "value":"syllabus"} of [mba]{"entity":"course", "value":"MBA-IT"}
- I want to know the [syllabus]{"entity":"course_feature", "value":"syllabus"} for [msc-ss]{"entity":"course", "value":"MSC-SS"}
- I want to know the [syllabus]{"entity":"course_feature", "value":"syllabus"} of [msc-ca]{"entity":"course", "value":"MSC-CA"}

##intent:ask_objectives
- what are the main [objectives]{"entity":"course_feature","value":"objectives"}
- what are the main [objectives]{"entity":"course_feature","value":"objectives"} of [msc-ca]{"entity":"course", "value":"MSC-CA"}
- what are the main [objectives]{"entity":"course_feature","value":"objectives"} for [bba]{"entity":"course", "value":"BBA-IT"}
- what are the main [objectives]{"entity":"course_feature","value":"objectives"} for [mba]{"entity":"course", "value":"MBA-IT"}
- what are the main [objectives]{"entity":"course_feature","value":"objectives"} of [msc-ca]{"entity":"course", "value":"MSC-CA"}
- what are the main [objectives]{"entity":"course_feature","value":"objectives"} for [msc-ss]{"entity":"course", "value":"MSC-SS"}

##intent:ask_outcomes
- what are the principal [outcomes]{"entity":"course_feature","value":"program outcomes"}
- what are the principal [outcomes]{"entity":"course_feature","value":"program outcomes"} of the course [bba-it]{"entity":"course","value":"BBA-IT"}
- what are the principal [outcomes]{"entity":"course_feature","value":"program outcomes"} for the course [mba-it]{"entity":"course","value":"MBA-IT"}
- what are the principal [outcomes]{"entity":"course_feature","value":"program outcomes"} of the course [bca]{"entity":"course","value":"BCA"}
- what are the principal [outcomes]{"entity":"course_feature","value":"program outcomes"} of the course [msc-ca]{"entity":"course","value":"MSC-CA"}
- what are the principal [outcomes]{"entity":"course_feature","value":"program outcomes"} for the course [msc-ss]{"entity":"course","value":"MSC-SS"}

<!-- ## intent:ask_selection+ask_eligibility
- i want to know the [eligibility]{"entity":"admin_feature","value":"eligibility criteria"} and [selection criteria]{"entity":"admin_feature","value":"selection procedure"}
- i want to know the [eligibility]{"entity":"admin_feature","value":"eligibility criteria"} and [selection criteria]{"entity":"admin_feature","value":"selection procedure"} for the course [bca]{"entity":"course","value":"BCA"}

## intent:ask_application+ask_selection
-  i want to know the [application process]{"entity":"admin_feature","value":"how to apply"} and the [selection procedure]{"entity":"admin_feature","value":"selection procedure"}
- i want to know the [application process]{"entity":"admin_feature","value":"how to apply"} and the [selection procedure]{"entity":"admin_feature","value":"selection procedure"} for [bba]{"entity":"course","value":"BBA-IT"}

## intent:ask_fees+ask_syllabus
- i want to know the [fees structure]{"entity":"admin_feature","value":"fees structure"} and the [syllabus]{"entity":"course_feature","value":"syllabus"}
- i want to know the [syllabus]{"entity":"course_feature","value":"syllabus"} and [fees structure]{"entity":"admin_feature","value":"fees structure"}
- i want to know the [syllabus]{"entity":"course_feature","value":"syllabus"} and [fees structure]{"entity":"admin_feature","value":"fees structure"} for [bba-it]{"entity":"course","value":"BBA-IT"}

## intent:ask_selection+ask_syllabus
- i want to know the [selection procedure]{"entity":"admin_feature","value":"selection procedure"} and [syllabus]{"entity":"course_feature","value":"syllabus"}
- i want to know the [syllabus]{"entity":"course_feature","value":"syllabus"} and [selection procedure]{"entity":"admin_feature","value":"selection procedure"}
- i want to know the [syllabus]{"entity":"course_feature","value":"syllabus"} and [selection procedure]{"entity":"admin_feature","value":"selection procedure"} for [bca]{"entity":"course","value":"BCA"}

## intent:ask_application+ask_syllabus
- i want to know the [application process]{"entity":"admin_feature","value":"how to apply"} and [syllabus]{"entity":"course_feature","value":"syllabus"}
- i want to know the [syllabus]{"entity":"course_feature","value":"syllabus"} and [application process]{"entity":"admin_feature","value":"how to apply"}
- i want to know the [syllabus]{"entity":"course_feature","value":"syllabus"} and [application process]{"entity":"admin_feature","value":"how to apply"} for [msc-ca]{"entity":"course","value":"MSC-CA"}

## intent:ask_eligibility+ask_syllabus
- i want to know the [eligibility criteria]{"entity":"admin_feature","value":"eligibility criteria"} and [syllabus]{"entity":"course_feature","value":"syllabus"}
- i want to know the [syllabus]{"entity":"course_feature","value":"syllabus"} and [eligibility criteria]{"entity":"admin_feature","value":"eligibility criteria"}
-  i want to know the [syllabus]{"entity":"course_feature","value":"syllabus"} and [eligibility criteria]{"entity":"admin_feature","value":"eligibility criteria"} for [bca]{"entity":"course","value":"BCA"} -->
