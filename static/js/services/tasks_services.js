export const getTasks = () => {
  return fetch("http://127.0.0.1:5000/getTasks", {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    method: "POST",
    body: {},
  }).then((response) => response.json())
  .then(data => {
      console.log(data);
  })
  .catch(error => console.log('error: ', error));
};
