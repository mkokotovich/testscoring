import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import Item from './Item';

import './ItemList.css';

class ItemList extends Component {
  constructor(props) {
    super(props);
    this.itemRefs = {};
  }

  componentDidUpdate(prevProps) {
    if (prevProps.items === undefined && this.props.items) {
      // This is the first time the items have been displayed, focus the first item
      this.changeFocus(-1);
    }
  }

  changeFocus = (index) => {
    if (this.props.items.length > (index + 1)) {
      if (this.itemRefs[index + 1]) {
        this.itemRefs[index + 1].focus();
      }
    }
  }

  render() {
    var itemInputs = [];
    if (this.props.items) {
      itemInputs = this.props.items.map((item, index) =>
        <Item
          key={index}
          item={item}
          inputRef={(el) => {
            this.itemRefs[index] = el;
          }}
          index={index}
          changeFocus={this.changeFocus}
          readonly={this.props.readonly}
          verify={this.props.verify}
          updateConflicts={this.props.updateConflicts}
        /> 
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
