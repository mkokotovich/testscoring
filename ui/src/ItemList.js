import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col, Modal, Input } from 'antd';
import './ItemList.css';

class ItemList extends Component {
  render() {
    var itemInputs = [];
    if (this.props.items) {
      itemInputs = this.props.items.map(item =>
        <div key={item.number}>
          <Row>
            <Col>
              {item.description}
            </Col>
            <Col>
              <Input
                value={item.score}
              />
            </Col>
          </Row>
        </div>
      );
    }

    return (
      <div className="ItemList">
        {itemInputs}
      </div>
    );
  }
}

export default withRouter(ItemList);
