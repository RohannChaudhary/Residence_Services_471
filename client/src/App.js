import Login from "./components/HomePage/Login";
import Homie from "./components/Home"
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Login />,
    },
    {
      path: "/home",
      element: <Homie />,
    },
  ]);
  return (
    <>
      <RouterProvider router = {router}/>
    </>
  );
}

export default App;
