import logo from './logo.svg';
import './App.css';
import MainMenu from './Pages/mainMenu';
import Webbrowser from './Pages/webbrowser';
import { BrowserRouter, Routes, Route } from "react-router-dom";



function App() {

  const rootElement = document.getElementById("root");


  return (
    <div className="App">
      <header className="App-header">

      </header>
      <body className="App-body">
      
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<MainMenu/>} />
            <Route path="/webbrowser" element={<Webbrowser/>} />
          </Routes>
        </BrowserRouter>

        
      </body>
    </div>
  );
}

export default App;
