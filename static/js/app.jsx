import React, { useState, useEffect } from "react";
import Button from "./components/button";
import { getTasks } from "./services/tasks_services";

const App = () => {
  useEffect(() => {
    getTasks
      .then((response) => {
        console.log("response: ", response);
      })
      .catch((error) => console.log("error: ", error));
  }, []);

  return (
    <>
      <Button />
    </>
  );
};

export default App;
