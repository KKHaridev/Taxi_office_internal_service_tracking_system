import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { Login } from "@driver/Login";
import { Dashboard } from "@driver/Dashboard";
import { Layout } from "@components";
import { AuthProvider } from "./context/AuthContext.jsx";
import { RequireLogin } from "./components/RequireLogin";

function App() {
  return (
    <>
      <AuthProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route
              path="/"
              element={
                <RequireLogin>
                  <Layout />
                </RequireLogin>
              }
            >
              <Route index element={<RequireLogin>
                  <Dashboard />
                </RequireLogin>} />
            </Route>
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </>
  );
}

export default App;
