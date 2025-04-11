import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Input, Button } from 'antd';
import './Search.css';

function Search(props) {
  const navigate = useNavigate();

  const searchByID = (value) => {
    navigate(`/tests/?search=${value}`);
  }

  const viewAll = () => {
    navigate("/tests/");
  }

  return (
    <div className="Search" style={{ marginBottom: 5}}>
      <Input.Search
        placeholder="Search by Client ID"
        enterButton="Search"
        style={{ width: 250 }}
        onSearch={value => searchByID(value)}
      />
      <Button style={{ marginLeft: 5 }} onClick={viewAll} >All Tests</Button>
    </div>
  );
}

export default Search;
