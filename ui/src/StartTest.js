import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, Button, Modal, Spin, Input } from 'antd';
import axios from 'axios';
import './StartTest.css';

function StartTest(props) {
  const [visible, setVisible] = useState(false);
  const [clientID, setClientID] = useState(undefined);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate()

  const showModal = () => {
    setVisible(true);
  }

  const viewExisting = () => {
    navigate(`/tests/?type=${props.assessment.slug}`);
  }

  const handleOk = (e) => {
    setLoading(true);
    var test_data = {
      client_number: clientID,
      test_type: props.assessment.slug
    }
    axios.post('/api/testing/v1/tests/', test_data)
      .then((response) => {
        console.log(response);
        setLoading(false);
        setVisible(false);
        navigate(`/tests/${response.data.id}/edit`);
      })
      .catch((error) => {
        console.log(error);
        setLoading(false);
        setVisible(false);
        Modal.error({
          title: "Unable to start a new scoring",
          content: "Unable to start a new scoring. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  const handleCancel = (e) => {
    setVisible(false);
  }

  const onChangeClientID = (e) => {
    setClientID(e.target.value);
  }

  return (
    <div className="StartTest">
      <Card style={{ width: 350 }}>
        <h1>{props.assessment.name}</h1>
        <div align="right">
          <Button type="primary" onClick={showModal}>Start New</Button>
          &nbsp;
          <Button type="primary" onClick={viewExisting}>View Existing</Button>
        </div>
        <Modal
          title={"Start a new " + props.assessment.name + " scoring"}
          visible={visible}
          onOk={handleOk}
          okText="Start"
          okButtonProps={{ disabled: !clientID }}
          onCancel={handleCancel}
        >
          <div align="center">
            { loading && <Spin size="large" />}
          </div>
          <p>Please enter the client ID</p>
          <Input
            placeholder="Enter Client ID"
            value={clientID}
            onChange={onChangeClientID}
            onPressEnter={() => handleOk()}
          />
        </Modal>
      </Card>
    </div>
  );
}

export default StartTest;
