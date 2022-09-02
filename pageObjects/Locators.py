ACCOUNT = {
    'account_icon': '//a[@class="ng-binding"]',
    'settings': 'crpo-common-settings',
    'new_form': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/ul/li[18]/span/b'
}

LOADING = {
    'load': 'dw-loading-active',
    'load_text': 'dw-loading-text',
    'upload': '//*[@ng-disabled="vm.loadingOptions.active"]',
    'embrace_load': '//*[@aria-busy="true"]',
    'candidate_load': 'block-ui-message'
}

TAG = {
    'anchor': 'a',
    'h2': 'h2',
    'h4': 'h4',
    'h5': 'h5',
    'h6': 'h6',
    'href': 'href',
    'p': 'p'
}

CHECK_BOX = {
    'check_box': '//input[@type="checkbox"]',
}

MENU = {
    'menu': "//a[contains(text(),'{}')]",
    'embrace': '//*[@ng-click="vm.invokeOtherApp(value.click)"]'
}

SUB_MENU = {
    'configurations': '//*[@ui-sref="crpo.events.details.configurations"]',
    'owners': '//*[@crpo.events.details.owners]',
    'event_tracking': '//*[@ui-sref="crpo.events.details.tracking"]',
    'cancel_request': '//*[@ui-sref="crpo.events.details.tracking.interviewCancelRequest"]',
    'job_configurations': '//*[@ui-sref="crpo.jobRole.details.configurations"]',
    'automations': '//*[@ui-sref="crpo.jobRole.details.automations.applicants"]',
    'job_owners': '//*[@ui-sref="crpo.jobRole.details.interviewers"]',
    'req_configurations': '//*[@ng-click="vm.goToConfiguration()"]',
    'req_duplicity': '//*[@ui-sref="crpo.requirements.details.configuration.candidateDuplicity"]',
    'req_query': '//*[@ui-sref="crpo.requirements.details.configuration.queryConfiguration"]',
    'nominations': '//*[@ui-sref="crpo.events.interviewers.nominations"]',
    'candidate_communication': '//*[@ui-sref="crpo.candidates.details.communicationDetails"]'
}

ATTACHMENT = {
    'file': '//input[@type="file"]',
    'multi_file': '(//input[@type="file"])[{}]'
}

NOTIFIER = {
    'message': 'growl-message',
    'dismiss': 'close'
}

PLACEHOLDER = {
    'place_holder': '//input[@placeholder="{}"]',
    'all_place_holder': '//*[@placeholder="{}"]',
    'text_ph': '//input[@type="text"][@placeholder="{}"]',
    'num_ph': '//input[@type="number"][@placeholder="{}"]',
    'num': '//input[@type="number"]'
}

TITLE = {
    'title': '//*[@title="{}"]',
    'tooltip': '//*[@bs-tooltip="{}{}{}"]'
}

CHECKBOX = {
    'check': 'grid_items',
    'type': '//*[@type="checkbox"]',
    'all': '//*[@ng-model="vm.isAllSelected"]'
}

BUTTONS = {
    'button': "//button[text()='{}']",
    'all_buttons': "//*[text()='{}']",
    'done': '//*[@ng-click="$hide();"]',
    'radio': 'label.btn-default',
    'actionClicked': '//*[@ng-click="vm.actionClicked({}{}{});"]',
    'btnActionClicked': '//*[@ng-click="vm.actionClicked({}{}{})"]',
    'create': '//*[@ng-click="vm.create();"]',
    'form_search': '//*[@ng-click="vm.service.templates.search();"]',
    'new_form_search': '.form-control.btn-submit',
    'ec_save': '//button[@ng-click="vm.saveEcConfig();"]',
    'task_configure': '//*[@ng-click="vm.getTaskConfigurationModal()"]',
    'close': '//*[@ng-click="vm.cancelClicked()"]',
    'add_criteria': '//button[@ng-click="vm.addCriteria()"]',
    'nomination_int_search': '//button[@ng-click="criterion.searchInterviewers()"]',
    'nomination_mail': '//button[@ng-click="vm.sendMailToAll()"]',
}

ACTIONS = {
    'actions_click': "//span[contains(text(),'Actions')]",
    'view_candidates': 'Event-Details-View-Candidates',
    'upload_candidate': 'Event-Details-Upload-Candidates',
    'event_owners': 'Event-Details-Manage-Event-Owners',
    'manage_interviewers': 'Event-Details-Manage-Interviewers',
    'live_interviews': 'Event-Details-Live-Schedule-Interviews',
    'event_interviews': 'Event-Details-View-Event-Interviews',
    'slot_config': 'Event-Details-Configure-Interview-Slots',
    'status_change': 'cardlist-view-Change-Applicant Status',
    'lobby': 'Event-Details-View-Interview-Lobby',
    'panel': 'Event-Details-View-Interview-Panel',
    'selection_process': 'Jobrole-Details-Selection-Process',
    'feedback_form': 'Jobrole-Details-Configure-Feedback-Form',
    'tag_interviewers': 'Jobrole-Details-Interviewers',
    'clone_assessment': 'Assessment-Details-Clone-Assessment',
    'app_more': '//*[@data-toggle="dropdown"]',
    'provide_feedback': 'cardlist-view-Provide-Interview Feedback',
    'cancel_request': 'cardlist-view-Cancel-Interview Request',
    'cancel_interview': 'cardlist-view-Cancel-Interview',
    'unlock_feedback': 'cardlist-view-Unlock-Interviewer Feedback',
    'float_click_class': 'fa-angle-right',
}

BUCKET = {
    'event_interviews': '//select[@ng-model="vm.config.selectedEntityType"]'
}

SEARCH = {
    'advance_search': 'cardlist-view-filter',
    'Name': 'Name',
    'name': 'name',
    'test_name': 'testName',
    'candidate_name': 'candidateName',
    'manage_candidate_search': '.fa-filter',
    'clear': 'cardlist-view-clear-filter',
}

MULTI_SELECTIONS = {
    'moveSelectedItemsRight': '//*[@data-ng-click="vm.moveSelectedItemsRight();"]',
    'moveAllItemsRight': '//*[@data-ng-click="vm.moveAllItemsRight();"]',
    'moveSelectedItemsLeft': '//*[@data-ng-click="vm.moveSelectedItemsLeft();"]',
    'moveAllItemsLeft': '//*[@data-ng-click="vm.moveAllItemsLeft();"]',
}

LOGIN = {
    'alias': 'alias',
    'next': '.btn-default',
    'login_name': 'loginName',
    'c_user_name': 'username',
    'password': '//input[@type="password"]',
    'login': 'login',
    'logout': 'crpo-settings-logout',
    'click_to_login': '//a[@ng-click="vm.backToLogin()"]',
    'e_login': '//*[@ng-click="vm.login()"]'
}

JOB = {
    'job_name': '//*[@placeholder="Name"]',
    'description': '//*[@id="mainBodyElement"]/div[3]/section/div/basic-job/div/div'
                   '[2]/div[8]/div/wysiwyg-edit/div/div[2]/iframe',
    'openings': 'openings',
    'feedback_overall_mandatory': '//table/tbody/tr[2]/td[2]/div/label[1]',
    'reject_overall_mandatory': '//table/tbody/tr[3]/td[2]/div/label[1]',
    'Ec_negative_stage': '//table/tbody/tr/th[4]/ta-dropdown/div/div/input',
    'Ec_negative_status': '//table/tbody/tr/th[5]/ta-dropdown/div/div/input',
    'task_new': 'addnew_link',
    'int_panel': '//*[@ng-model="vm.selectedInterviewPanel"]',
    'panel_int_add': 'add_label',
    'total_owners': '.section_header.ng-binding',
    'registration_hop': '//*[@id="main-table"]/tbody[1]/tr[2]/td[1]/div/i',
    'eligibility_hop': '//*[@id="main-table"]/tbody[2]/tr[2]/td[1]/div/i',
    'offer_stage': '//*[@id="main-table"]/tbody[7]/tr[4]/td[1]/div/i',
    'hop_stage_field': '//*[@ng-model="vm.hopping[statusId].selectedStage"]',
    'hop_status_field': '//*[@ng-model="vm.hopping[statusId].selectedStatus"]',
    'toggle_buttons': '(//*[@class="switch"])[{}]'
}

CHANGE_STATUS = {
    'stage': '//*[@ng-model="vm.selectedStage"]',
    'status': '//*[@ng-model="vm.selectedStatus"]',
    'comment': '//*[@ng-model="vm.comments"]'
}

CANDIDATE = {
    'id': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[2]/p[2]/span[2]',
    'upload_signature': '//*[@ng-model="vm.signature"]',
    'name_field': '//*[@id="mainBodyElement"]/div[7]/div/div/div[2]/form/div[1]/div/input',
    'email_field': '//*[@id="mainBodyElement"]/div[7]/div/div/div[2]/form/div[3]/div/input',
    'usn_field': '//*[@id="mainBodyElement"]/div[7]/div/div/div[2]/form/div[9]/div/input',
    'save_info': '//*[@data-ng-click="vm.validateSingleCandidate(entity);"]',
    'Upload_count': '.status-card.bg-success.ng-binding',
    'save': '//*[@data-ng-click="vm.consolidateCandidateInfo();"]',
    'certificates': '(//*[@ng-repeat="certification in vm.data.certificationDetails"])[{}]',
    'education': '(//strong[@class="ng-binding"])[{}]',
    'other_attachments': '(//a[@class="property-label"])[{}]',
    'id_card_verified': '(//td[@class="th ng-scope"])[2]',
    'down_arrow': '(//i[@class="fa fa-chevron-down"])[1]'
}

EVENT = {
    'comment_cancel_request': '//textarea[@ng-model="data.comments"]'
}

EVENT_LOBBY = {
    'active': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Activate Room', "'"),
    'assign_slot': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Assign slots', "'"),
    'un_assign': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Unassign Room', "'"),
    'assign_room': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Assign Room', "'"),
    'room_search': 'noDataMsg',
}

CANDIDATE_LOBBY_LOGIN = {
    'candidate_name': "//label[contains(text(),'{}')]",
    'queued-message': "/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]",
    'almost-message': ".headerText.ng-scope",
    'your-message': '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]',
    'finished-message': '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/p[1]'
}

LIVE_INTERVIEW = {
    'stage_selection': '//*[@ng-model="vm.selectedInterviewStage"]',
    'app_search': '//*[@ng-click="vm.searchApplicants();"]',
    'clear_search': '//button[@ng-click="vm.clearSearch();"]',
    'int_screen': 'modal-header',
    'select_int': '//*[@ng-readonly="vm.config.readonly"]',
    'arrow_down': 'fa-chevron-down',
    'feedback_button': '//*[@ng-click="data.onGiveFeedbackClick(rowKey);"]'
}

FEEDBACK = {
    'select_drop_down': '//select[@ng-model="row.rowOptions.selectedRating"]',
    'decision_button': '//*[@ng-repeat="option in vm.resultStatusOptions"]',
    'comments': '//textarea[@ng-model="row.rowOptions.skillComment"]',
    'select_int': '//*[@ng-readonly="vm.config.readonly"]',
    'overall': '//*[@ng-model="vm.finalTranscript"]',
    'submit': '//*[@ng-click="vm.submitFeedback(vm.isUpdateFeedback);"]',
    'new_form_drop_down': '//*[@ng-model="question.answer.dropdownCode"]',
    'save_draft': '//button[@ng-click="vm.saveDraft();"]',
    'partial': '//button[@ng-click="vm.partialSubmitFeedback();"]',
    'update': '//*[@ng-click="vm.submitFeedback(vm.isUpdateFeedback);"]'
}

INTERVIEWER_LOBBY = {
    'finish_interview': '//*[@id="mainBodyElement"]/div[7]/div/div/div/div[2]/div[1]/button'
}

MANAGE_TASK = {
    'common_label': '.ng-binding',
    'candidate_status': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[1]/span[2]',
    'total': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[5]'
}

EMBRACE = {
    'candidate_tab': '/html/body/div[1]/header[2]/div/div/div[2]/div/ul/li[2]/a',
    'candidate_name_search_field': '//*[@ng-model="vm.candidateSearchCriteria.CandidatName"]',
    'candidate_acceptance_yes': 'testacceprtanceoffer'
}

HELPDESK = {
    'job_category': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/div/div[1]'
                    '/div[2]/div/div/table/tbody/tr/td[1]/div/span/span/span[1]',
    'event_category': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/div/div[1]'
                      '/div[3]/div/div/table/tbody/tr/td[1]/div/span/span/span[1]',
    'job_sla': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/div/div[1]/div[2]'
               '/div/div/table/tbody/tr/td[4]/input',
    'event_sla': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/div/div[1]/div[3]'
                 '/div/div/table/tbody/tr/td[5]/input',
    'job_user': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/div/div[1]/div[2]'
                '/div/div/table/tbody/tr/td[3]/div/span/span/span[1]',
    'event_user': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/div/div[1]/div[3]'
                  '/div/div/table/tbody/tr/td[4]/div/span/span/span[1]',
    'event_job': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/div/div[1]/div[3]'
                 '/div/div/table/tbody/tr/td[2]/div/span/span/span[1]'
}

QUERY = {
    'more_queries': '//*[@ui-sref="candidate.helpdesk.raiseQuery"]',
    'category_select': '//*[@ng-change="vm.processQueries();"]',
    'subject_field': '//*[@ng-model="vm.subject"]',
    'message_field': '//*[@ng-model="vm.messasge"]',
    'status_bucket': '//*[@ng-model="vm.querySearchCriteria.QueryStatus"]'
}

NOMINATIONS = {
    'panel_1': "//input[@type='text']",
    'panel_2': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/'
               'transcluded-input/div/div/div/div/div[1]/ta-dropdown/div/div/input',
    'search': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/'
              'transcluded-input/div/div/div/div/div[4]/button',
    'skill1_int': '//input[@ng-model="criterion.requiredInterviewers"]',
    'skill2_int': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/'
                  'transcluded-input/div/div/div[1]/div[2]/div/div[1]/input',
    'skill1_nom': '//input[@ng-model="criterion.requiredNominations"]',
    'skill2_nom': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/'
                  'transcluded-input/div/div/div[1]/div[2]/div/div[2]/input',
    'dropdown': 'fa-chevron-down',
    'panel_select': '//select[@ng-model="vm.selectedSearchPanelType"]',
    'actions': 'btn-submit',
    'approve': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/div[1]/div[2]/ul/li[1]/a'
}

MICROSITE = {
    'first_name': 'firstName',
    'middle_name': 'middleName',
    'last_name': 'lastName',
    'pan_number_filed': 'panNo',
    'card_type': 'idCardType',
    'whatsapp_consent': '//select[@ng-model="vm.service.formData[property.id]"]',
    'certificationType': '(//select[@ng-model="certification.certificationType.value"])[{}]',
    'certificateName': '(//select[@ng-model="certification.certificationName.value"])[{}]',
    'certificateStatus': '(//select[@ng-model="certification.certificationStatus.value"])[{}]',
    'institute': '(//select[@ng-model="certification.certificationInstitution.value"])[{}]',
    'from_month': '(//select[@ng-model="certification.fromMonth.value"])[{}]',
    'to_month': '(//select[@ng-model="certification.toMonth.value"])[{}]',
    'from_year': '(//select[@ng-model="certification.fromYear.value"])[{}]',
    'to_year': '(//select[@ng-model="certification.toYear.value"])[{}]',
    'text_ph': '(//input[@type="text"][@placeholder="No Of Attempts"])[{}]',
    'pg_type': 'Education Type0',
    'pg_degree': 'Degree0',
    'pg_college': 'College0',
    'pg_branch': 'Branch0',
    'pg_yop': 'Year Of Passing0',
    'pg_cgpa_radio': 'CGPA0',
    'pg_cgpa': 'isPercentage0',
    'pg_out_of': 'percentageOutOf0',
    'ug_type': 'Education Type1',
    'ug_degree': 'Degree1',
    'ug_college': '(//*[@ng-model="education.college.value"])[2]',
    'ug_branch': 'Branch1',
    'ug_yop': 'Year Of Passing1',
    'ug_percent_radio': 'Percentage1',
    'ug_percent': 'isPercentage1',
    '12th_type': 'Education Type2',
    '12th_yop': 'Year Of Passing2',
    '12th_cgpa_radio': 'CGPA2',
    '12th_cgpa': 'isPercentage2',
    '10th_type': 'Education Type3',
    '10th_yop': 'Year Of Passing3',
    '10th_percent_radio': 'Percentage3',
    '10th_percent': 'isPercentage3',
}
