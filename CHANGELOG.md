Changelog
=========


(unreleased)
------------

New
- Run only one test method or class (v1.0.1) [ylesueur]
- Get_selected_org and get_selected_team instead of Factories.
  [ylesueur]
- Change log file (0.0.4) [ylesueur]
- Config file for gitchangelog API. [ylesueur]
- Makefile to init envrionement and run tests (0.0.4) [ylesueur]
- Requirements folder with dev and prod files. [ylesueur]

Changes
- Versionning (1.0.1) [Jordan martin]
- Use test_helper methods instead of TeamFactory or OrgUserPK.
  [ylesueur]
- Use test_helper methods instead of TeamFactory or OrgUserPK.
  [ylesueur]
- Use test_helper methods instead of TeamFactory or OrgUserPK.
  [ylesueur]
- Use test_helper methods instead of TeamFactory or OrgUserPK.
  [ylesueur]
- Use test_helper methods instead of TeamFactory or OrgUserPK.
  [ylesueur]
- Use test_helper methods instead of TeamFactory or OrgUserPK.
  [ylesueur]
- Use test_helper methods instead of TeamFactory or OrgUserPK.
  [ylesueur]
- Move TeamFactory and OrguserPkFactory into test_helper. [ylesueur]
- Remove pytest warning with the attribute __test__=False (0.0.4)
  [ylesueur]
- Need to fix create_invoice_item (0.0.4) [ylesueur]
- Python for first test (0.0.4) [ylesueur]
- Requirements folder  (0.0.4) [ylesueur]
- Remove dead links from table index. [ylesueur]
- Rules ordering (0.0.4) [ylesueur]
- Move requirements.txt into requirements folder. [ylesueur]
- Get the selected organisation instead of the first one. [ylesueur]
- Add flake8, autopep8 in dev dependancies. [ylesueur]

Fix
- Add a clean object Invoice to create_invoice_item and
  delete_invoice_item. [ylesueur]
- __get_selected_org should be called before __get_teams to avoid None
  pk. [ylesueur]
  variable (0.0.4) [ylesueur]

Other
- Feat(changelog): Add changelog. [Jordan martin]
- Feat(folders-name): Change folder name, little fix in makefile.
  [Jordan martin]
- Merge pull request #31 from axonepro/0.0.4. [Max Riahi]

  Fix tests
- Fix tests. [Baptiste Vincent]
- Merge pull request #28 from axonepro/0.0.4. [Max Riahi]

  0.0.4
- Fix HelperHelper error. [Baptiste Vincent]
- Fix test_helper error. [Baptiste Vincent]
- Fix merge conflicts. [Baptiste Vincent]
- Merge pull request #26 from axonepro/0.0.3. [Max Riahi]

  0.0.4
- Merge pull request #25 from ylesueur-ooti/0.0.4. [Max Riahi]

  Fixing test and move into tests folder
- Merge branch 'master' into 0.0.4. [Baptiste Vincent]
- Merge pull request #23 from axonepro/0.0.3. [Max Riahi]

  0.0.3
- Fix for deploy 1.0.0. [Baptiste VINCENT]
- Merge pull request #27 from axonepro/structuration. [Baptiste Vincent]

  Structuration
- Fix tests. [Baptiste VINCENT]
- Fix tests. [Baptiste VINCENT]
- Remove warning test_helper. [Baptiste VINCENT]
- Fix tests. [Baptiste VINCENT]
- Fix README. [Baptiste VINCENT]
- Fix ci. [Baptiste VINCENT]
- Add teardown() functions + fix tests. [Baptiste VINCENT]
- Fill more resources + add all new tests to travis and makefile.
  [Baptiste VINCENT]
- Separate tests depending on the associated resource. [Baptiste
  VINCENT]
- Fix tests + Add test_time to travis and makefile. [Baptiste VINCENT]
- Fix tests. [Baptiste VINCENT]
- Fill last resources + delete ooti folder. [Baptiste VINCENT]
- Fill more resources. [Baptiste VINCENT]
- Move logo + remove example.py file + put example in README. [Baptiste
  VINCENT]
- Fill more resources. [Baptiste VINCENT]
- Add parameter argument for process_request method. [Baptiste VINCENT]
- Fill more resources + add process_request method + replace all
  requests. [Baptiste VINCENT]
- All requests replaced by call of process_request method. [Baptiste
  VINCENT]
- Fill costs, employees, expenses and jobs. [Baptiste VINCENT]
- Add all python files. [Baptiste VINCENT]
- Fix travis. [Baptiste VINCENT]
- Try to fix tests. [Baptiste Vincent]
- Removed __init__.py for pytest. [ylesueur]
- Fixed parent package error on import ooti module. [ylesueur]
- Contrib.md is a guideline to contributors of the sdk. [ylesueur]
- Change Log. [ylesueur]
- Added a Developer section. [ylesueur]
- Changelog. [ylesueur]
- Fix seleted orguser pk and set trips_enabled to True before testing.
  [ylesueur]
- Ignore flake8 and setup.cfg file. [ylesueur]
- Ignore flake8 and setup.cfg file. [ylesueur]
- Moved test into tests folder. [ylesueur]
- Tests moved into tests folder. [ylesueur]
- Added Flake8. [ylesueur]
- Ignore .ENV files. [ylesueur]
- Remove FreelancerTest which does not exist anymore. [ylesueur]
- Add a class to get orguser_pk. [ylesueur]
- Exclude test files from package. [ylesueur]
- Following import convention. [ylesueur]
- Fix test with TeamFactory as team selected. [ylesueur]
- Fix format string on second parameters: 1 instead of 0. [ylesueur]
- Fix test: selected right team and org. [ylesueur]
- Removed useless team selected -> factories/TeamFactory does same.
  [ylesueur]
- Move factories into new package. [ylesueur]
- Move test into separate folder. [ylesueur]
- New Folder for tests. [ylesueur]
- Get selected user team and merge with selected org method. [ylesueur]
- Version 0.0.4. [yoles]
- Add new private method to get the user selected organization. [yoles]
- Merge pull request #22 from axonepro/fixing-tests-sdk. [Max Riahi]

  Fixing tests
- Fixing tests. [Thomas]
- :memo: commented uncleaned app. [vinsJ]
- :hammer: fix auth on factories. [vinsJ]
- :hammer: fix auth with ENV variables. [vinsJ]
- Merge branch '0.0.3' of https://github.com/axonepro/sdk-ooti into
  0.0.3. [vinsJ]
- Merge pull request #21 from axonepro/pagination. [Max Riahi]

  Add Pagination
- Merge branch '0.0.3' into pagination. [Max Riahi]
- :memo: add dotenv in requirements. [vinsJ]
- :memo: remove comments. [vinsJ]
- :memo: remove comments and print. [vinsJ]
- :rocket: feat_pagination. [vinsJ]
- Merge branch '0.0.3' into pagination. [vinsJ]
- :construction: WIP - Add pagination. [vinsJ]
- :pushpin: add version to dotenv. [vinsJ]
- :memo: update requirements.txt. [vinsJ]
- :construction_worker: Add Travis to project. [vinsJ]
- :see_no_evil: update base_url based on ENV variable. [vinsJ]
- :memo: update test_helper. [vinsJ]
- :memo: update names. [vinsJ]
- Merge pull request #19 from axonepro/CU-ag553f_Time_Vincent-Debande.
  [Max Riahi]

  Cu ag553f time vincent debande
- :rocket: :art: refactor and improved test / fixed SDK. [vinsJ]
- Merge pull request #20 from axonepro/CU-a229pe_Thomas-SDK-
  Notes_Thomas-REY. [Max Riahi]

  Notes SDK + Fixing 500 in costs, auth, collaboration, setting and others
- Addind notes to custom fields. [Thomas]
- Fixing all remaining 500. [Thomas]
- Update costs.py. [Thomas]
- Update test_costs.py. [Thomas]
- Update .gitignore. [Thomas]
- Adding contractor factory. [Thomas]
- Testing others, settings, collaboration and auth. [Thomas]
- Fixing costs sdk. [Thomas]
- Testing expenses. [Thomas]
- Testing SDK. [Thomas]
- Merge pull request #18 from axonepro/CU-ag14d3_Deliverables_Vincent-
  Debande. [Max Riahi]

  Cu ag14d3 deliverables vincent debande
- :rocket: :art: improve tests fixed errors. [vinsJ]
- Merge pull request #17 from axonepro/CU-ae44ue_Vincent-SDK-
  Notes_Vincent-Debande. [Max Riahi]

  Cu ae44ue vincent sdk notes vincent debande - invoicing
- :art: refactor and improve testing. [vinsJ]
- :rocket: add file creation. [vinsJ]
- :hammer: fix currencies urls. [vinsJ]
- :construction: :art: WIP - Add helper test ("factory") and refactored
  tests into classes. [vinsJ]
- :cloud: :memo: changed python version. [vinsJ]

  #a229pv[DOING]
- Update readme. [Maxime Riahi]
- Merge pull request #15 from axonepro/features-billing. [Max Riahi]

  Feat - Plans, Prescriptions, Defaults, Documents, Contracts, Revisions, Annexes, Phases, Timeperiods, Timeoff, Timelogs, Roles, Trips, Revenue (Invoicing)
- :hammer: fix test. [vinsJ]
- Merge branch 'master' into features-billing. [vinsJ]
- Merge pull request #16 from axonepro/thomas. [Max Riahi]

  Finishing others methods and reorganizing code
- Finishing others methods. [Thomas]
- Adding more projections methods. [Thomas]
- Reorganizing code. [Thomas]
- Merge pull request #14 from axonepro/thomas. [Max Riahi]

  Adding posts, expenses, jobs methods
- Adding goals and indicators methods. [Thomas]
- Finishing settings methods. [Thomas]
- Adding actions, billing and celery_tasks methods. [Thomas]
- Updating comments. [Thomas]
- Adding costs methods. [Thomas]
- Adding employees methods. [Thomas]
- Finishing jobs methods. [Thomas]
- Adding expenses and jobs methods. [Thomas]
- Adding posts methods. [Thomas]
- Merge pull request #13 from axonepro/thomas. [Max Riahi]

  Finishing contacts and adding newsletters & notes methods
- Finishing contacts and adding newsletters & notes methods. [Thomas]
- Merge pull request #10 from axonepro/thomas. [Max Riahi]

  Projects and orgusers methods added
- Fixing bugs and adding more contact methods. [Thomas]
- Merge branch 'thomas' of https://github.com/axonepro/sdk-ooti into
  thomas. [Thomas]
- Merge branch 'master' into thomas. [Thomas]
- Merge pull request #12 from axonepro/features-billing. [Max Riahi]

  Features billing - Refactor code
- Merge pull request #11 from axonepro/features-billing. [Max Riahi]
- Merge pull request #9 from axonepro/features-billing. [Max Riahi]

  Feat - INVOICING: Emails
- Adding tasks methods. [Thomas]
- Reorganizing code. [Thomas]
- Adding more project methods. [Thomas]
- Adding invitations methods. [Thomas]
- Adding permissions methods. [Thomas]
- Finishing project methods. [Thomas]
- Adding team and profile methods. [Thomas]
- Projects and orgusers methods added. [Thomas]
- Merge pull request #8 from axonepro/features-billing. [Max Riahi]

  Features billing
- :hammer: :memo: fix method | update doc. [vinsJ]
- :hammer: fix method. [vinsJ]
- :hammer: fix method. [vinsJ]
- :white_check_mark: :memo: :hammer: add tests | update doc | fix test.
  [vinsJ]
- :memo: update doc. [vinsJ]
- :white_check_mark: :memo: add tests | update doc. [vinsJ]
- :hammer: :memo:  fix input functions  | update doc. [vinsJ]
- :memo: add bugs and status errors at the beginning. [vinsJ]
- :white_check_mark: add tests revenue. [vinsJ]
- :rocket: feat - revenue. [vinsJ]
- :white_check_mark: add tests trips. [vinsJ]

  Cannot create trips, 403
- :rocket: feat - trips. [vinsJ]
- :white_check_mark: add tests for roles. [vinsJ]
- :rocket: feat - roles. [vinsJ]
- :white_check_mark: add tests for timeoff. [vinsJ]

  And remove tests that don't pass
- :hammer: fix post functions and add payload. [vinsJ]
- :white_check_mark: add tests for timeperiods. [vinsJ]

  Some tests don't pass
- :rocket: feat - timeperiods. [vinsJ]
- :memo: update comment. [vinsJ]
- :rocket: implement time in SDK. [vinsJ]
- :white_check_mark: add tests time. [vinsJ]
- :rocket: feat - time. [vinsJ]
- :memo: remove "# * OK" [vinsJ]
- :memo: remove "# * OK" [vinsJ]
- :white_check_mark: add tests Phases, fees, plan_details, Contracts,
  Revisions. [vinsJ]
- :rocket: feat planphase, adapt code. [vinsJ]
- :white_check_mark: add tests annexes and revisions (not complete)
  [vinsJ]
- :rocket: feat revisions (not all tested) and annexes. [vinsJ]
- :white_check_mark: :construction: add some tests contracts
  (uncomplete) [vinsJ]
- :rocket: feat contracts. [vinsJ]
- :white_check_mark: add tests plans. [vinsJ]
- :white_check_mark: add tests documents and :hammer: fix test. [vinsJ]
- :rocket: feat documents. [vinsJ]
- :memo: update doc (remove TODO) [vinsJ]
- :art: :white_check_mark: refactor tests into scripts | add tests for
  defaults. [vinsJ]
- :rocket: feat defaults. [vinsJ]
- :white_check_mark: add tests prescriptions. [vinsJ]
- :rocket: feat prescriptions | [vinsJ]
- :hammer: fix a test. [vinsJ]
- :art: :construction: adapt code to refactorisation. Add a few tests
  for plans (not complete) [vinsJ]
- :rocket: feat - plans (untested) [vinsJ]

  Could not test because could not create plans: 'code' field required and unknown
- :art: refactor deliverables. [vinsJ]
- :art: :construction: refactor code. [vinsJ]

  Separate functions in files
- :white_check_mark: add tests Zones, :construction:  Fees. [vinsJ]
- :rocket: feat - zones and fees. [vinsJ]
- :white_check_mark: add tests: :x: areas, :construction: phases, :x:
  milestones. [vinsJ]

  Areas : update does not work (403)

  Milestones : get details does not work (403)
- :rocket: :construction: feat - Areas, Phases :construction: ,
  Milestones. [vinsJ]
- :white_check_mark: add tests styleguide. [vinsJ]
- :rocket: feat - styleguide (and beginning of revenue) [vinsJ]
- :white_check_mark: add tests reports. [vinsJ]
- :rocket: feat - reports. [vinsJ]
- :white_check_mark: add tests files and banks. [vinsJ]
- :rocket: feat - files and banks. [vinsJ]
- :white_check_mark: add tests emails endpoints. [vinsJ]
- :rocket: feat - email endpoints. [vinsJ]
- :rocket: :construction: feat - helper : process_response | emails.
  [vinsJ]
- :memo: update comments. [vinsJ]
- :art: refactor organization of code. [vinsJ]
- :memo: update page_size in requests (999999) [vinsJ]
- :white_check_mark: add tests get credit notes. [vinsJ]
- :rocket: feat - get credit notes. [vinsJ]
- :white_check_mark:  test get valid sent invoices. [vinsJ]
- :rocket: feat - get valid sent invoices. [vinsJ]
- :white_check_mark: add tests invoice. [vinsJ]
- :rocket: feat - send and close invoice. [vinsJ]
- Merge branch 'master' into features-billing. [vinsJ]
- Merge pull request #7 from axonepro/contacts. [Max Riahi]

  Adding contact methods
- Correcting contact deletion. [Thomas]
- Correcting contact deletion. [Thomas]
- Adding contact methods. [Thomas]
- Adding contact methods. [Thomas]
- Merge branch 'master' into features-billing. [vinsJ]
- Merge pull request #6 from axonepro/features-billing. [Max Riahi]
- Merge pull request #5 from axonepro/features-billing. [Max Riahi]
- Merge pull request #4 from axonepro/thomas. [Max Riahi]
- Merge pull request #3 from axonepro/thomas. [Max Riahi]

  Update returns
- Merge pull request #2 from axonepro/thomas. [Max Riahi]
- :white_check_mark: add tests invoice + payment. [vinsJ]
- :rocket: feat - validate invoice. [vinsJ]
- :white_check_mark: test invoice update + invoice items. [vinsJ]
- :rocket: feat- invoice items. [vinsJ]
- :memo: better spaces for separators. [vinsJ]
- :memo: update comment separator. [vinsJ]
- :see_no_evil: add test_sdk.py. [vinsJ]
- :hammer: fix test. [vinsJ]
- Merge remote-tracking branch 'origin/thomas' into features-billing.
  [vinsJ]
- Updating teams_pk attribute. [Thomas]
- Adding teams attribute. [Thomas]
- Adding annexe methods. [Thomas]
- :white_check_mark: :construction:  add invoices test. [vinsJ]
- :memo: update doc create_client. [vinsJ]
- :white_check_mark: add tests currency and client. [vinsJ]
- :rocket: feat- get team id. [vinsJ]
- :memo: update outputs of invoice and payment. [vinsJ]
- :rocket: feat client functions. [vinsJ]
- :twisted_rightwards_arrows: :rocket: merge with features-thomas
  (update returns) + feat currency methods. [vinsJ]
- :cloud: setup pipenv. [vinsJ]
- :see_no_evil: update .gitignore. [vinsJ]
- Update returns. [Thomas]
- Adding token methods. [Thomas]
- Correcting creation of invoices. [Thomas]
- Change readme. [Hippolyte Bringer]
- Change url logo. [Hippolyte Bringer]
- Change name. [Hippolyte Bringer]
- Add doc. [Hippolyte Bringer]
- Change setup and readme. [Hippolyte Bringer]
- Change infra. [Hippolyte Bringer]
- Update README.md. [Max Riahi]
- Update README.md. [Max Riahi]
- Update README.md. [Max Riahi]
- Add payment and change readme. [Hippolyte Bringer]
- Change invoice + readme. [Hippolyte Bringer]


