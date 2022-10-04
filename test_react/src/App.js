import logo from './logo.svg';
import './App.css';

import React, {useEffect, useState} from 'react';

function App() {
  const [num, setNum] = useState("11111");

  useEffect(()=>{
    setNum(2);
    // 下载数据
  }, [num]);
  

  console.log('1');

  return (
    <div className="App">
      <p>num: {num}</p>
      <button onClick={()=>{setNum('a')}}>setNum</button>
    </div>
  );
}

export default App;
