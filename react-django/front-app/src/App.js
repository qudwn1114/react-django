import logo from './logo.svg';
import './App.css';

function App() {

  function testApi(txt) {
    const queryString = `?text=${txt}`;
    fetch(`http://127.0.0.1:8000/api/test/${queryString}`, {
          method: "GET"
        })
          .then(response => response.json())
          .then(data => {
            alert('통신성공..');
            console.log(data);
          });
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button style={{fontSize: "3rem" }} onClick={ async ()=> testApi('test')}>
          api test!!!
        </button>
      </header>
    </div>
  );
}

export default App;
