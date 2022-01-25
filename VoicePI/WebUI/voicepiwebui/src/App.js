import './App.css';
import MainMenu from './Pages/mainMenu';
import Webbrowser from './Pages/webbrowser';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Help from './Pages/Help';
import ImageDisp from './Pages/imagedisp';
import SilentMode from './Pages/silentmode';
import Capture from './Pages/Capture';
import Weather from './Pages/Weather';


function App() {



  return (
    <div className="App">
      <header className="App-header">

      </header>
      <body className="App-body">
      
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<MainMenu/>} />
            <Route path="/webbrowser" element={<Webbrowser/>} />
            <Route path="/help" element={<Help/>} />
            <Route path="/image" element={<ImageDisp/>} />
            <Route path="/silentmode" element={<SilentMode/>} />
            <Route path="/capture" element={<Capture/>} />
            <Route path="/wetter" element={<Weather/>} />
          </Routes>
        </BrowserRouter>

        
      </body>
    </div>
  );
}

export default App;
