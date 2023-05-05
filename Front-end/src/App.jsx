import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { Login } from "@driver/Login";
import { Dashboard } from "@driver/Dashboard";
import { Layout } from "@components";
import { AuthProvider } from "@context/AuthContext.jsx";
import { RequireLogin } from "@components/RequireLogin";
import { Test } from "@driver/Test";

function App() {
  return (
    <>
      <AuthProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/" element={<Layout />}>
              <Route
                index
                element={
                  <RequireLogin>
                    <Dashboard />
                  </RequireLogin>
                }
              />
              <Route
                path="test"
                element={
                  <RequireLogin>
                    <Test />
                  </RequireLogin>
                }
              />
            </Route>
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </>
  );
}

export default App;
