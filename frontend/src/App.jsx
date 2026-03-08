import React, { useEffect, useState } from 'react';
import './App.css';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://54.196.48.241:8000/api/getall", {
        method: "GET",
        headers: { 'Content-Type': 'application/json' }
      })
      .then(response => {
        if (!response.ok) 
          throw new Error(response.status + " " + response.statusText);
        return response.json();
      })
      .then(res => {setData(res.data); })
      .catch(err => { alert(err);});
  }, []);


  return (
    <div className='app'>
      <table>
        <tr>
          <th>ID</th>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Phone Number</th>
          <th>Email ID</th>
        </tr>
        {data.map((student, index)=>(
          <tr key={index}>
            <td>{student.id}</td>
            <td>{student.firstname}</td>
            <td>{student.lastname}</td>
            <td>{student.phone}</td>
            <td>{student.emailid}</td>
          </tr>
        ))}
      </table>
    </div>
  );
}

export default App;