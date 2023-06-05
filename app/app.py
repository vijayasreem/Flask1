Flask API

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']

        # Validate user credentials and login
        if user is not None and password is not None:
            return redirect(url_for('expert_services'))
        else:
            flash('Username and password are required!')
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/expert_services', methods=['GET', 'POST'])
def expert_services():
    if request.method == 'POST':
        # User clicks on Configure
        if request.form['submit'] == 'Configure':
            return redirect(url_for('jira_software'))
        # User clicks on Reset
        elif request.form['submit'] == 'Reset':
            return redirect(url_for('expert_services'))
    else:
        return render_template('expert_services.html')

@app.route('/jira_software', methods=['GET', 'POST'])
def jira_software():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        url = request.form['url']
        repository = request.form['repository']

        # Validate JIRA credentials
        if username is not None and password is not None and url is not None and repository is not None:
            # Validate with Java API
            response = validate_credentials(username, password, url, repository)
            if response is not None and response == 'success':
                # Save JIRA credentials
                save_credentials(username, password, url, repository)
                # Get list of configured JIRA accounts
                accounts = get_accounts()
                # Render list of configured JIRA accounts
                return render_template('jira_software.html', accounts=accounts)
            else:
                flash('Invalid JIRA credentials!')
                return render_template('jira_software.html')
        else:
            flash('All fields are required!')
            return render_template('jira_software.html')
    else:
        return render_template('jira_software.html')

@app.route('/edit_account/<id>', methods=['GET', 'POST'])
def edit_account(id):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        url = request.form['url']
        repository = request.form['repository']

        # Validate JIRA credentials
        if username is not None and password is not None and url is not None and repository is not None:
            # Validate with Java API
            response = validate_credentials(username, password, url, repository)
            if response is not None and response == 'success':
                # Update JIRA credentials
                update_credentials(id, username, password, url, repository)
                # Get list of configured JIRA accounts
                accounts = get_accounts()
                # Render list of configured JIRA accounts
                return render_template('jira_software.html', accounts=accounts)
            else:
                flash('Invalid JIRA credentials!')
                return render_template('jira_software.html')
        else:
            flash('All fields are required!')
            return render_template('jira_software.html')
    else:
        # Get account details
        account = get_account(id)
        # Render form with account details
        return render_template('edit_account.html', account=account)

@app.route('/delete_account/<id>', methods=['GET', 'POST'])
def delete_account(id):
    if request.method == 'POST':
        # Delete JIRA account
        delete_account(id)
        # Get list of configured JIRA accounts
        accounts = get_accounts()
        # Render list of configured JIRA accounts
        return render_template('jira_software.html', accounts=accounts)
    else:
        # Get account details
        account