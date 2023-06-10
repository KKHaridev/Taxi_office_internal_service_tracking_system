import jwt_decode from "jwt-decode";
import { createContext, useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const navigate = useNavigate();

  let [user, setUser] = useState(() =>
    localStorage.getItem("authTokens")
      ? jwt_decode(localStorage.getItem("authTokens"))
      : null
  );
  let [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem("authTokens")
      ? JSON.parse(localStorage.getItem("authTokens"))
      : null
  );

  let [loading, setLoading] = useState(true);

  let login = async (formValues) => {
    let response = await fetch("http://127.0.0.1:8000/authapi/token/", {
      method: "POST",
      body: JSON.stringify({
        username: formValues.name,
        password: formValues.password,
      }),
      headers: {
        Accept: "*/*",
        "Content-Type": "application/json",
      },
    });

    let data = await response.json();
    if (response.status == 200) {
      setAuthTokens(data);
      setUser(jwt_decode(data.access));
      localStorage.setItem("authTokens", JSON.stringify(data));
      navigate("/", { replace: true });
    } else {
      alert("Something went wrong");
    }
  };

  let updateToken = async () => {
    let response = await fetch("http://127.0.0.1:8000/authapi/token/refresh/", {
      method: "POST",
      body: JSON.stringify({
        refresh: authTokens?.refresh,
      }),
      headers: {
        Accept: "*/*",
        "Content-Type": "application/json",
      },
    });

    let data = await response.json();
    if (response.status == 200) {
      setAuthTokens(data);
      setUser(jwt_decode(data.access));
      localStorage.setItem("authTokens", JSON.stringify(data));
    } else {
      setUser(null);
      setAuthTokens(null);
      localStorage.removeItem("authTokens");
    }
    if (loading) {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (loading) {
      updateToken();
    }
    let fourmin = 1000 * 60 * 4;
    let interval = setInterval(() => {
      if (authTokens) {
        updateToken();
      }
    }, fourmin);
    return () => clearInterval(interval);
  }, [authTokens, loading]);

  const logout = () => {
    setUser(null);
    setAuthTokens(null);
    localStorage.removeItem("authTokens");
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {loading ? null : children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
