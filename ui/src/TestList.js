import React, { useState, useEffect } from 'react';
import { useParams, useLocation } from 'react-router-dom';
import { Button, Modal, Spin, Divider } from 'antd';
import Test from './Test';
import Search from './Search';
import axios from 'axios';
import queryString from 'query-string';
import './TestList.css';

function TestList(props) {

  const [tests, setTests] = useState([]);
  const [loading, setLoading] = useState(false);
  const { testId } = useParams();
  const location = useLocation();

  useEffect(() => {
    loadTests();
  }, []);

  useEffect(() => {
    setTests([]);
    loadTests();
  }, [location.search]);

  const loadTests = () => {
    setLoading(true);
    const values = queryString.parse(location.search);
    var query = "";
    var sep = "?";
    if (values.type) {
      query = `${query}${sep}test_type=${values.type}`;
      sep = "&";
    }
    if (values.search) {
      query = `${query}${sep}search=${values.search}`;
      sep = "&";
    }
    if (values.clientid) {
      query = `${query}${sep}client_number=${values.clientid}`;
      sep = "&";
    }
    axios.get(`/api/testing/v1/tests/${query}`)
      .then((response) => {
        console.log(response);
        setLoading(false);
        setTests(response.data);
      })
      .catch((error) => {
        console.log(error);
        setLoading(false);
        Modal.error({
          title: "Unable to load tests",
          content: "Unable to load tests. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  const updateStateWithNewTest = (newTest) => {
    const updatedTests = tests.map((test) => {
      if (test.id === newTest.id) {
        return newTest;
      } else {
        return test;
      }
    });
    setTests(updatedTests);
  }

  const handleArchiveAll = () => {
    console.log("archiving all tests");
    setLoading(true);
    axios.post(`/api/testing/v1/tests/archiveall/`)
      .then((response) => {
        setLoading(false);
        console.log(response);
        setTests(response.data);
      })
      .catch((error) => {
        console.log(error);
        setLoading(false);
        Modal.error({
          title: "Unable to archive all tests",
          content: "Unable to archive all tests. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  const handleArchive = (testId) => {
    setLoading(true);
    console.log("archive " + testId);
    axios.post(`/api/testing/v1/tests/${testId}/archive/`)
      .then((response) => {
        setLoading(false);
        console.log(response);
        updateStateWithNewTest(response.data);
      })
      .catch((error) => {
        setLoading(false);
        console.log(error);
        Modal.error({
          title: "Unable to archive test",
          content: "Unable to archive test. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  const handleRestore = (testId) => {
    console.log("restore " + testId);
    setLoading(true);
    axios.post(`/api/testing/v1/tests/${testId}/restore/`)
      .then((response) => {
        setLoading(false);
        console.log(response);
        updateStateWithNewTest(response.data);
      })
      .catch((error) => {
        setLoading(false);
        console.log(error);
        Modal.error({
          title: "Unable to restore test",
          content: "Unable to restore test. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  const handleDelete = (testId) => {
    console.log("delete " + testId);
    setLoading(true);
    axios.delete(`/api/testing/v1/tests/${testId}/`)
      .then((response) => {
        setLoading(false);
        console.log(response);
        const newTests = tests.filter(item => item.id !== testId);
        setTests(newTests);
      })
      .catch((error) => {
        setLoading(false);
        console.log(error);
        Modal.error({
          title: "Unable to delete test",
          content: "Unable to delete test. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  const expandedRowRender = (record) => {
    return (
      <div>
        Created at: {record.created_at} and last modified at: {record.updated_at}
      </div>
    )
  }

  const displayTests = tests.map(test =>
    <div key={test.id}>
      <Test
        test={test}
        handleArchive={handleArchive}
        handleRestore={handleRestore}
        handleDelete={handleDelete}
        assessmentBySlug={props.assessmentBySlug}
      />
      <Divider />
    </div>
  );
  return (
    <div className="TestList">
      <Search/>
      <div align="center">
        { loading && <Spin size="large" />}
      </div>
      <Divider />
      {displayTests}
      <Button onClick={handleArchiveAll}>Archive All Tests</Button>
    </div>
  );
}

export default TestList;
