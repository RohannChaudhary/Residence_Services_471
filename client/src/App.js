import Login from "./components/HomePage/Login";
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";
import Fairy from "./components/Fairy";
import Maintenance from "./components/Maintenance";
import Profile from "./components/Profile";

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Login />,
    },
    {
      path: "/Fairy",
      element: <Fairy />,
    },
    {
      path: "/Maintenance",
      element: <Maintenance />,
    },
    {
      path: "/Profile",
      element: <Profile />,
    },
  ]);
  return (
    <>
      <RouterProvider router = {router}/>
    </>
  );
}

export default App;
