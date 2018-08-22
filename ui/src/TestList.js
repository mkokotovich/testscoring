import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col } from 'antd';
import './TestList.css';

class TestList extends Component {
  render() {
    return (
      <div className="TestList">
        List all CBCL tests
      </div>
    );
  }
}

export default withRouter(TestList);
