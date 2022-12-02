import Login from "./components/HomePage/Login";
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";
import Maintenance from "./components/Maintenance";
import Profile from "./components/Profile";
import Dashboard from "./components/Dashboard";
import Complaints from "./components/Complaints";

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Login />,
    },
    {
      path: "/dashboard",
      element: <Dashboard />,
    },
    {
      path: "/Maintenance",
      element: <Maintenance />,
    },
    {
      path: "/Profile",
      element: <Profile />,
    },
    {
      path: "/complaints",
      element: <Complaints />,
    },
  ]);
  return (
    <>
      <RouterProvider router = {router}/>
    </>
  );
}

export default App;
