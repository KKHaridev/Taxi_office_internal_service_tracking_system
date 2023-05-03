import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { Login } from "@driver/Login";
import { Dashboard } from "@driver/Dashboard";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />}></Route>
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
