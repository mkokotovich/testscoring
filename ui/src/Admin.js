import React, { useState, useEffect } from 'react';
import { withRouter } from 'react-router-dom';
import { Row, Col, Input, Modal, Spin, Divider} from 'antd';
import queryString from 'query-string';
import axios from 'axios';
import './Admin.css';

function Admin(props) {
  const [loading, setLoading] = useState(false);
  const [users, setUsers] = useState([]);

  const loadUsers = () => {
    setLoading(true);
    axios.get('/api/users/v1/')
      .then((response) => {
        setLoading(false);
        console.log(response);
        setUsers(response.data);
      })
      .catch((error) => {
        setLoading(false);
        console.log(error);
        Modal.error({
          title: "Unable to load users",
          content: "Unable to load users. Please refresh page and try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  };

  useEffect(() => {
    loadUsers();
  }, [props.user]);

  const displayedUsers = users.map(user =>
    <div key={user.id}>
      {user.id} {user.username} {user.first_name} {user.last_name}
      <Divider />
    </div>
  );

  return (
    <>
      <h1>Users</h1>
      {displayedUsers}
    </>
  );

}

export default withRouter(Admin);
