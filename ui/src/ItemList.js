import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
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
