ACCOUNT = {
    'account_icon': '//a[@class="ng-binding"]',
    'settings': 'crpo-common-settings',
    'new_form': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/ul/li[18]/span/b'
}

LOADING = {
    'load': 'dw-loading-active',
    'load_text': 'dw-loading-text',
    'upload': '//*[@ng-disabled="vm.loadingOptions.active"]'
}

TAG = {
    'anchor': 'a',
    'h4': 'h4',
    'href': 'href'
}

CHECK_BOX = {
    'check_box': '//input[@type="checkbox"]',
}

MENU = {
    'menu': "//a[contains(text(),'{}')]"
}

SUB_MENU = {
    'configurations': '//*[@ui-sref="crpo.events.details.configurations"]',
    'owners': '//*[@crpo.events.details.owners]',
    'job_configurations': '//*[@ui-sref="crpo.jobRole.details.configurations"]',
    'automations': '//*[@ui-sref="crpo.jobRole.details.automations.applicants"]'
}

ATTACHMENT = {
    'file': '//input[@type="file"]'
}

NOTIFIER = {
    'message': 'growl-message',
    'dismiss': 'close'
}

PLACEHOLDER = {
    'place_holder': '//input[@placeholder="{}"]',
    'text_ph': '//input[@type="text"][@placeholder="{}"]',
    'num_ph': '//input[@type="number"][@placeholder="{}"]'
}

TITLE = {
    'title': '//*[@title="{}"]'
}

CHECKBOX = {
    'check': 'grid_items'
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
    'ec_save': '//button[@ng-click="vm.saveEcConfig();"]'
}

ACTIONS = {
    'actions_click': "//span[contains(text(),'Actions')]",
    'view_candidates': 'Event-Details-View-Candidates',
    'slot_config': 'Event-Details-Configure-Interview-Slots',
    'status_change': 'cardlist-view-Change-Applicant Status',
    'lobby': 'Event-Details-View-Interview-Lobby',
    'panel': 'Event-Details-View-Interview-Panel',
    'selection_process': 'Jobrole-Details-Selection-Process',
    'feedback_form': 'Jobrole-Details-Configure-Feedback-Form',
    'float_click_class': 'fa-angle-right',
    'float_action': ''
}

SEARCH = {
    'advance_search': 'cardlist-view-filter',
    'Name': 'Name',
    'name': 'name',
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
    'password': '//input[@type="password"]',
    'login': 'login',
    'logout': 'crpo-settings-logout',
    'click_to_login': '//a[@ng-click="vm.backToLogin()"]'
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
    'task_new': 'addnew_link'
}

CHANGE_STATUS = {
    'stage': '//*[@ng-model="vm.selectedStage"]',
    'status': '//*[@ng-model="vm.selectedStatus"]',
    'comment': '//*[@ng-model="vm.comments"]'
}

CANDIDATE = {
    'id': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[2]/p[2]/span[2]'
}

EVENT_LOBBY = {
    'active': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Activate Room', "'"),
    'assign_slot': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Assign slots', "'"),
    'un_assign': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Unassign Room', "'"),
    'assign_room': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Assign Room', "'"),
    'room_search': 'noDataMsg'
}

CANDIDATE_LOBBY_LOGIN = {
    'candidate_name': "//label[contains(text(),'{}')]",
    'queued-message': "/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]",
    'almost-message': ".headerText.ng-scope",
    'your-message': '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]',
    'finished-message': '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/p[1]'
}

FEEDBACK = {
    'select_drop_down': '//select[@ng-model="row.rowOptions.selectedRating"]',
    'decision_button': '//*[@ng-repeat="option in vm.resultStatusOptions"]',
    'comments': '//textarea[@ng-model="row.rowOptions.skillComment"]',
    'overall': '//*[@ng-model="vm.finalTranscript"]',
    'submit': '//*[@ng-click="vm.submitFeedback(vm.isUpdateFeedback);"]',
}

INTERVIEWER_LOBBY = {
    'finish_interview': '//*[@id="mainBodyElement"]/div[7]/div/div/div/div[2]/div[1]/button'
}
