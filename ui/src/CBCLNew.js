import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col } from 'antd';
import './CBCLNew.css';

class CBCLNew extends Component {
  render() {
    return (
      <div className="CBCLNew">
        Create a new CBCL scoring!
      </div>
    );
  }
}

export default withRouter(CBCLNew);
