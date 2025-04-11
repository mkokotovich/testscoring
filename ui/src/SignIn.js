import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Modal, Button, Dropdown, Menu } from 'antd';
import axios from 'axios';
import decode from 'jwt-decode';

import SignInForm from './SignInForm'


function SignOut(props) {
  const menuClick = ({ key }) => {
    if (key === "signout") {
      props.handleSignOut();
    } else if (key === "profile") {
      props.handleProfile();
    }
  };

  const menu = (
    <Menu onClick={menuClick}>
      <Menu.Item key="profile">Profile</Menu.Item>
      <Menu.Item key="signout">Sign Out</Menu.Item>
    </Menu>
  );

  return (
    <React.Fragment>
      <Dropdown overlay={menu} placement="bottomRight">
        <Button type="default" icon="user">
          {props.username}
        </Button>
      </Dropdown>
    </React.Fragment>
  );
}

function SignIn(props) {
  const navigate = useNavigate();
  const [isSignedIn, setIsSignedIn] = useState(false);
  const [username, setUsername] = useState(undefined);

  useEffect(() => {
    // Check if token exists and isn't expired
    const token = localStorage.getItem('id_token');
    if (token) {
      const decoded = decode(token);
      const current_time = new Date().getTime() / 1000;
      if (decoded.exp && decoded.exp < current_time) {
	/* Token is expired, sign out */
	handleSignOut();
      } else {
	signInWithToken(token);
      }
    }
    const user = localStorage.getItem('user');
    if (user) {
      const user_obj = JSON.parse(user)
      props.handleAuthChange(user_obj);
      setUsername(user_obj.username);
    }
  }, []);

  const signInWithToken = (token) => {
    localStorage.setItem('id_token', token);
    axios.defaults.headers.common['Authorization'] = "Bearer " + token;
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.xsrfHeaderName = "X-CSRFToken";
    setIsSignedIn(true);
  }

  const handleSignIn = (username, password) => {
    console.log("Trying to sign in " + username);
    axios.post('/api/auth/', {
      username: username,
      password: password
    })
    .then((response) => {
      const token = response.data.token;
      const user = response.data.user;
      console.log(response.headers);
      if (token) {
	console.log("Signed in " + username);
	setUsername(username);
	signInWithToken(token);
	if (user) {
	  localStorage.setItem('user', JSON.stringify(user));
	  props.handleAuthChange(user);
	}
      } else {
	console.log("Failed to sign in " + username);
	Modal.error({
	  title: "Unable to sign in",
	  content: "Please check username and password and try again",
	  maskClosable: true,
	})
      }
    })
    .catch((error) => {
      console.log(error);
      Modal.error({
	title: "Unable to sign in",
	content: "Please check username and password and try again",
	maskClosable: true,
      })
    });
  }

  const handleProfile = () => {
    navigate("/profile");
  }

  const handleSignOut = () => {
    localStorage.removeItem("id_token");
    localStorage.removeItem("user");
    setUsername(undefined);
    props.handleAuthChange(null);
    delete axios.defaults.headers.common["Authorization"];

    console.log("Signed out");
    setIsSignedIn(false);
    navigate("/");
  }

  const signInOrOut = isSignedIn ? (
    <SignOut handleSignOut={handleSignOut} handleProfile={handleProfile} username={username} />
  ) : (
    <SignInForm handleSignIn={handleSignIn} />
  );

  return (
    <div className="SignIn">
      {signInOrOut}
    </div>
  );
}

export default SignIn
