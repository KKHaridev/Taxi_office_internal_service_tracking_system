import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { Login } from "@driver/Login";
import { Dashboard } from "@driver/Dashboard";
import { Layout } from "@components";
import { AuthProvider } from "@context/AuthContext.jsx";
import { RequireLogin } from "@components/RequireLogin";
import { RideRequests } from "@driver/RideRequests";

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
                path="received_rides"
                element={
                  <RequireLogin>
                    <RideRequests />
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
