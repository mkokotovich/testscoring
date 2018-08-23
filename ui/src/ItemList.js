import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col, Modal, Input } from 'antd';
import Item from './Item';

import './ItemList.css';

class ItemList extends Component {
  render() {
    var itemInputs = [];
    if (this.props.items) {
      itemInputs = this.props.items.map(item =>
        <Item item={item} /> 
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
