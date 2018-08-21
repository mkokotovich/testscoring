import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col } from 'antd';
import './CBCLList.css';

class CBCLList extends Component {
  render() {
    return (
      <div className="CBCLList">
        List all CBCL tests
      </div>
    );
  }
}

export default withRouter(CBCLList);
