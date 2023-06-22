import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { Login } from "@driver/Login";
import { Dashboard } from "@driver/Dashboard";
import { Layout } from "@components";
import { AuthProvider } from "@context/AuthContext.jsx";
import { RequireLogin } from "@components/RequireLogin";
import { RideRequests } from "@driver/RideRequests";
import { Ongoing } from "@driver/Ongoing";
import { Completed } from "@driver/Completed";
import { Canceled } from "@driver/Canceled";
import { Earnings } from "@driver/Earnings";
import { ViewRideRequests } from "@components/ViewRideRequests";
import { Profile } from "@driver/Profile";

import { AdminLogin } from "@admin/AdminLogin";
import { CarsAndDrivers } from "./admin/CarsAndDrivers";
import { CarsAndDriversDetails } from "./admin/CarAndDriverDetails";

function App() {
  return (
    <>
      <BrowserRouter>
        <AuthProvider>
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
              <Route
                path="received_rides/:id"
                element={
                  <RequireLogin>
                    <ViewRideRequests />
                  </RequireLogin>
                }
              />
              <Route
                path="Ongoing_rides"
                element={
                  <RequireLogin>
                    <Ongoing />
                  </RequireLogin>
                }
              />
              <Route
                path="ongoing_rides/:id"
                element={
                  <RequireLogin>
                    <ViewRideRequests />
                  </RequireLogin>
                }
              />
              <Route
                path="completed_rides"
                element={
                  <RequireLogin>
                    <Completed />
                  </RequireLogin>
                }
              />
              <Route
                path="completed_rides/:id"
                element={
                  <RequireLogin>
                    <ViewRideRequests />
                  </RequireLogin>
                }
              />
              <Route
                path="canceled_rides"
                element={
                  <RequireLogin>
                    <Canceled />
                  </RequireLogin>
                }
              />
              <Route
                path="earnings"
                element={
                  <RequireLogin>
                    <Earnings />
                  </RequireLogin>
                }
              />
              <Route
                path="profile"
                element={
                  <RequireLogin>
                    <Profile />
                  </RequireLogin>
                }
              />
            </Route>
          </Routes>

          {/* Admin */}
          <Routes>
            <Route path="/admin/login" element={<AdminLogin />} />
            <Route path="admin/" element={<Layout />}>
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
              <Route
                path="received_rides/:id"
                element={
                  <RequireLogin>
                    <ViewRideRequests />
                  </RequireLogin>
                }
              />
              <Route
                path="cars_and_drivers"
                element={
                  <RequireLogin>
                    <CarsAndDrivers />
                  </RequireLogin>
                }
              />
              <Route
                path="cars_and_drivers/:id"
                element={
                  <RequireLogin>
                    <CarsAndDriversDetails />
                  </RequireLogin>
                }
              />
              <Route
                path="Ongoing_rides"
                element={
                  <RequireLogin>
                    <Ongoing />
                  </RequireLogin>
                }
              />
              <Route
                path="ongoing_rides/:id"
                element={
                  <RequireLogin>
                    <ViewRideRequests />
                  </RequireLogin>
                }
              />
              <Route
                path="completed_rides"
                element={
                  <RequireLogin>
                    <Completed />
                  </RequireLogin>
                }
              />
              <Route
                path="completed_rides/:id"
                element={
                  <RequireLogin>
                    <ViewRideRequests />
                  </RequireLogin>
                }
              />
              <Route
                path="canceled_rides"
                element={
                  <RequireLogin>
                    <Canceled />
                  </RequireLogin>
                }
              />
              <Route
                path="earnings"
                element={
                  <RequireLogin>
                    <Earnings />
                  </RequireLogin>
                }
              />
              <Route
                path="profile"
                element={
                  <RequireLogin>
                    <Profile />
                  </RequireLogin>
                }
              />
            </Route>
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </>
  );
}

export default App;
