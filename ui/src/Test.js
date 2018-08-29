import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Button, Row, Col, Popconfirm, Icon } from 'antd';
import './Test.css';
import * as moment from 'moment';

class Test extends Component {
  state = {
  }

  componentDidMount() {
  }

  render() {

    return (
      <div className="Test">
        <Row type="flex" align="middle">
          <Col className="TestTitle TestDetail" xs={12} sm={6} md={4} >
            <Link to={{ pathname: `/tests/${this.props.test.id}/view` }} > Test {this.props.test.id}</Link>
          </Col>
          <Col className="TestDetail" xs={12} sm={6} md={4} >
            Client {this.props.test.client_number}
          </Col>
          <Col className="TestDetail" xs={6} sm={3} md={2} >
            <Link to={{ pathname: `/tests/${this.props.test.id}/verify` }} > Verify </Link>
            { this.props.test.verified ? 
              <Icon type="check-circle-o" style={{ fontSize: 16 }} /> :
              <Icon type="exclamation-circle-o" style={{ fontSize: 16 }} /> }
          </Col>
          <Col className="TestDetail" xs={6} sm={3} md={2} >
            <Link to={{ pathname: `/tests/${this.props.test.id}/scores` }} > Scores </Link>
          </Col>
          <Col className="TestDetail" xs={6} sm={3} md={2} >
            <Link to={{ pathname: `/tests/${this.props.test.id}/edit` }} > Edit </Link>
          </Col>
          <Col className="TestDetail" xs={6} sm={3} md={{span: 2, push: 8}} >
            <Popconfirm title="Really Delete?" onConfirm={() => this.props.handleDelete(this.props.test.id) }>
              <Button type="danger">Delete</Button>
            </Popconfirm>
          </Col>
          <Col className="TestDetail" xs={24} md={{span: 8, pull: 2}}>
            Created: {moment(this.props.test.created_at).calendar()}
          </Col>
        </Row>
      </div>
    );
  }
}

export default Test;
