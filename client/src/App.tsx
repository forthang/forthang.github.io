
import logo from './logo.svg';
import React from "react";
import ReactDOM from "react-dom";

const iframe = ''; 
  
function App() {
  
  return (
        <div>
            <div className="a" style={{position:"absolute"}}>
               <h1>Map Display</h1>
               <div className="li">1</div>
               <div className="li">2</div>
               <div className="li">3</div>
               <div className="li">4</div>
               <div className="li">5</div>
               <div className="li">6</div>
               <div className="li">7</div>
               <div className="li">8</div>
               <div className="li">9</div>
              </div>
            <iframe
                src="/map.html"
                title="Map"
                style={{ width: '85%', height: '100vh', border: 'none', bottom:'0', right: '0', position:'absolute'}}
            />
        </div>
  )

}




export default App;
