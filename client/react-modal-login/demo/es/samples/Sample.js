import React from 'react';
import ReactModalLogin from '../../../src/react-modal-login';
import ReactBubbleChart from 'react-bubble-chart';

import {facebookConfig, googleConfig} from "../social-config";
import axios from 'axios';

var donated = [];
var id = [];
var name = [];

export default class Sample extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      showModal: false,
      loggedIn: null,
      loading: false,
      error: null,
      initialTab: null,
      recoverPasswordSuccess: null,
    };

     this.onLogin = this.onLogin.bind(this)
  }


  onLogin() {
    console.log('__onLogin__');
    console.log('email: ' + document.querySelector('#email').value);
    console.log('password: ' + document.querySelector('#password').value);

    const email = document.querySelector('#email').value;
    const password = document.querySelector('#password').value;

    if (!email || !password) {
      this.setState({
        error: true
      })
    } else {
      this.onLoginSuccess('form');
    }

    // fetch('https://34.238.243.88:5000/')
    //   .then(response => {
    //     response.json()
    //     console.log(response.json);
    //   })
    //   .then(data => {
    //     console.log(data);
    //     this.setState(groups: data)
    //   })
    //   .catch((error) =>  {
    //     console.log(error);
    //   });

     axios.get('http://34.238.243.88:5000/groups/create/', {
      method: 'POST',
      mode: 'no-cors',
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        withCredentials: true,
        credentials: 'same-origin',
      }
    })
      .then(response => {
        console.log(response.data);
        console.log(response.data[0]);
        console.log(response.data[0].donated);
        console.log(response.data.length);
        for(let i = 0; i < response.data.length; i++) {
            donated.push(response.data[i].donated);
            id.push(response.data[i].id);
            name.push(response.data[i].name);
            console.log(donated[i]);
        }
        })
      .catch((error) =>  {
        console.log(error);
      })
  }

  onRegister() {
    console.log('__onRegister__');
    console.log('login: ' + document.querySelector('#login').value);
    console.log('email: ' + document.querySelector('#email').value);
    console.log('password: ' + document.querySelector('#password').value);

    const login = document.querySelector('#login').value;
    const email = document.querySelector('#email').value;
    const password = document.querySelector('#password').value;
    const industry = document.querySelector('#industry').value;

    if (!login || !email || !password) {
      this.setState({
        error: true
      })
    } else {
      this.onLoginSuccess('form');
    }
  }

  onRecoverPassword() {
    console.log('__onFotgottenPassword__');
    console.log('email: ' + document.querySelector('#email').value);

    const email = document.querySelector('#email').value;


    if (!email) {
      this.setState({
        error: true,
        recoverPasswordSuccess: false
      })
    } else {
      this.setState({
        error: null,
        recoverPasswordSuccess: true
      });
    }
  }

  openModal(initialTab) {
    this.setState({
      initialTab: initialTab
    }, () => {
      this.setState({
        showModal: true,
      })
    });
  }

  onLoginSuccess(method, response) {

    this.closeModal();
    this.setState({
      loggedIn: method,
      loading: false
    })
  }

  onLoginFail(method, response) {

    this.setState({
      loading: false,
      error: response
    })
  }

  startLoading() {
    this.setState({
      loading: true
    })
  }

  finishLoading() {
    this.setState({
      loading: false
    })
  }

  afterTabsChange() {
    this.setState({
      error: null,
      recoverPasswordSuccess: false,
    });
  }

  closeModal() {
    this.setState({
      showModal: false,
      error: null
    });
  }

  render() {

    const loggedIn = this.state.loggedIn
      ? <div>
          <p>You are signed in.</p>
        </div>
      : <div>
          <p></p>
      </div>;

    const isLoading = this.state.loading;

    return (
      <div>
        <div class="col-xs-9"></div>
        <div class = "col-xs-3">

        <button
          type="button"
          class="btn btn-success"
          onClick={() => this.openModal('login')}
          >Sign In/Sign Up</button>

        <br></br>

        </div>

        <p>{this.state.id}</p>

        <ReactModalLogin
          visible={this.state.showModal}
          onCloseModal={this.closeModal.bind(this)}
          loading={isLoading}
          initialTab={this.state.initialTab}
          error={this.state.error}
          tabs={{
            afterChange: this.afterTabsChange.bind(this)
          }}
          startLoading={this.startLoading.bind(this)}
          finishLoading={this.finishLoading.bind(this)}
          form={{
            onLogin: this.onLogin.bind(this),
            onRegister: this.onRegister.bind(this),
            onRecoverPassword: this.onRecoverPassword.bind(this),

            recoverPasswordSuccessLabel: this.state.recoverPasswordSuccess
              ? {
                  label: "New password has been sent to your mailbox!"
                }
              : null,
            recoverPasswordAnchor: {
              label: "Forgot your password?"
            },
            loginBtn: {
              label: "Sign in"
            },
            registerBtn: {
              label: "Sign up"
            },
            recoverPasswordBtn: {
              label: "Send new password"
            },
            loginInputs: [
              {
                containerClass: 'RML-form-group',
                label: 'Email',
                type: 'email',
                inputClass: 'RML-form-control',
                id: 'email',
                name: 'email',
                placeholder: 'Email',
              },
              {
                containerClass: 'RML-form-group',
                label: 'Password',
                type: 'password',
                inputClass: 'RML-form-control',
                id: 'password',
                name: 'password',
                placeholder: 'Password',
              }
            ],
            registerInputs: [
              {
                containerClass: 'RML-form-group',
                label: 'Username',
                type: 'text',
                inputClass: 'RML-form-control',
                id: 'login',
                name: 'login',
                placeholder: 'Username',
              },
              {
                containerClass: 'RML-form-group',
                label: 'Email',
                type: 'email',
                inputClass: 'RML-form-control',
                id: 'email',
                name: 'email',
                placeholder: 'Email',
              },
              {
                containerClass: 'RML-form-group',
                label: 'Password',
                type: 'password',
                inputClass: 'RML-form-control',
                id: 'password',
                name: 'password',
                placeholder: 'Password',
              },
              {
                containerClass: 'RML-form-group',
                label: 'Industry',
                type: 'texts',
                inputClass: 'RML-form-control',
                id: 'industry',
                name: 'industry',
                placeholder: 'Industry',
              }
            ],
            recoverPasswordInputs: [
              {
                containerClass: 'RML-form-group',
                label: 'Email',
                type: 'email',
                inputClass: 'RML-form-control',
                id: 'email',
                name: 'email',
                placeholder: 'Email',
              },
            ],
          }}
          separator={{
            label: "or"
          }}
          providers={{
            facebook: {
              config: facebookConfig,
              onLoginSuccess: this.onLoginSuccess.bind(this),
              onLoginFail: this.onLoginFail.bind(this),
              inactive: isLoading,
              label: "Continue with Facebook"
            },
            google: {
              config: googleConfig,
              onLoginSuccess: this.onLoginSuccess.bind(this),
              onLoginFail: this.onLoginFail.bind(this),
              inactive: isLoading,
              label: "Continue with Google"
            }
          }}
        />
        {loggedIn}
      </div>
    )
  }
}