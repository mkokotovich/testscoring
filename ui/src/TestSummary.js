import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col, Modal } from 'antd';
import './TestSummary.css';

class TestSummary extends Component {
  render() {
    var test = this.props.test;
    return (
      <div className="TestSummary">
        <Link to={`/tests/${test.id}/edit`}>
          Test {test.id}: {test.test_type} with client {test.client_number}
        </Link>
        <br/>
        Created at {test.created_at} and last modified at {test.updated_at}
      </div>
    );
  }
}

export default withRouter(TestSummary);
