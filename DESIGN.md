# Template hierarchy

1. when if user == null
template-basic.html

1. when if user != null and study == null
template-user.html

1. when if user != null and study != null
template-study.html



## Pages

1. `home.html`
	- extends `template-basic.html`
	- button goes to `home`

1. `login.html`
	- extends template-basic.html
	- success response redirects to the entrypoint (or `dashboard`)
	- context

	```
	{
		"redirect_to": "entrypointurl"
	}
	```

1. `mygroups.html`
	- extends `template-user.html`
	- context

	```
	{
		"groups": [

		]
	}
	```
	- goes to `create-or-edit-group.html` or `group-dashboard.html`

1. `create-group.html`
	- extends `template-user.html`
	- submit

	```
	{
		"name": "group name",
	}
	```

1. `edit-group.html`
	- extends `template-user.html`
	- context

	```
	{
		"group": non-null,
		"group-settings": nullable
	}
	```
	- submit

	```
	{
		"group": non-null,
		"group-settings": nullable // includes charge items
	}
	```

1. `create-group-result.html`
	- extends `template-user.html`
	- context

	```
	{
		"passcode": non-null
	}
	```
	- submit

	```
	{
		"emails": [ ]
	}
	```

1. `accept-invitation.html`
	- extends `template-user.html`
	- submit

	```
	{
		"passcode": Non-null
	}
	```

1. `group-dashboard.html`
	- extends `template-study.html`
	- context

	```
	{
		"sessions": [

		]
	}
	```

1. `edit-session.html`
	- extends `template-study.html`
	- Always create a session first, and then edit.
	- context

	```
	{
		"session": non-null,
		"members": []
	}
	```
	- submit

	```
	{
		"charges": []
	}
	```
	- DEL request


1. `group-setting-for-admin.html`
	- extends `template-study.html`
	- context

	```
	{
		"group": non-null,
		"settings": non-null
	}
	```
	- submit

	```
	{
		"group": non-null,
		"settings": non-null
	}
	```
	- DEL request


1. `edit-admin-list.html`
	- extends `template-study.html`
	- context

	```
	{
		"group": non-null,
		"members": [], (member.is_admin() should be available)
	}
	```
	- submit

	```
	{
		"group": non-null,
		"admins": [],
	}
	```

1. `account-page-for-admin.html`
	- extends `template-study.html`
	- context

	```
	{
		"group": non-null,
		"members": [], (member.is_admin() should be available)
	}
	```
	- submit 1 : N빵
	- submit 2 : specific account



1. `deposit.html`
	- extends `template-study.html`
	- context

	```
	{
		"group": non-null,
		"amount": amount-to-deposit,
		"bank-account": "bank-account"
	}
	```
	- button to go to kakaobank, toss or something else.
	- check button => AJAX

1. `withdraw.html`
	- extends `template-study.html`
	- context

	```
	{
		"group": non-null,
		"amount": amount to withdraw
	}
	```
	- submit withdraw request
