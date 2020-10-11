import React, { useState, useEffect } from "react";
import Button from "./components/button";
import { getTasks } from "./services/tasks_services";

const App = () => {
  useEffect(() => {
    fetch("http://127.0.0.1:5000/getTasks", {
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
      },
    })
      .then((response) => {
        console.log("response: ", response);
        return response.json();
      })
      .then((data) => console.log("data: ", data))
      .catch((error) => console.log("error: ", error));
  }, []);

  return (
    <>
      <Button />
    </>
  );
};

export default App;
