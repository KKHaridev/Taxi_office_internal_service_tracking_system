import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { Login } from "@driver/Login";
import { Dashboard } from "@driver/Dashboard";
import { Layout } from "@components";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/" element={<Layout />}>
            <Route index element={<Dashboard />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
