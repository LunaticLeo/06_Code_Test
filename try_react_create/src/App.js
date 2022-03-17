import { useState, useEffect } from 'react';

function App() {
  console.log("enter function component");

  const [attr, setAttr] = useState(0);

  useEffect(() => {
    console.log("enter useEffect");
  }, []);

  setTimeout(() => {
    setAttr(attr => attr + 1);
  }, 1000);

  return (<div>Counter: {attr}</div>);
}

export default App;
