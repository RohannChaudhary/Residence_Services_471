import React from "react";
import { useState } from "react";

async function loginUser(credentials) {
  return fetch('http://localhost:3000/studentdashboard', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
    .then(data => data.json())
 }

const Login = () => {
  const [username, setUserName] = useState();
  const [password, setPassword] = useState();

  const handleSubmit = async e => {
    e.preventDefault();
    const token = await loginUser({
      username,
      password
    });
  }

  return (
    <>
      <div className="flex h-screen">
        <div className="flex flex-1 flex-col justify-center py-12 px-4 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
          <div className="mx-auto w-full max-w-sm lg:w-96">
            <div>
              <img
                className="h-32 w-auto mx-auto"
                src="data:image/png;base64,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"
                alt="Your Company"
              />
              <h2 className="mt-6 text-3xl font-bold tracking-tight text-gray-900">
                Sign in to your UResidence account
              </h2>
            </div>

            <div className="mt-8">
              <div className="mt-6">
                <form action="#" method="POST" className="space-y-6">
                  <div>
                    <label
                      htmlFor="username"
                      className="block text-sm font-medium text-gray-700"
                    >
                      Username
                    </label>
                    <div className="mt-1">
                      <input
                        id="username"
                        name="username"
                        type="username"
                        rules={[
                          {
                            required: true,
                            message : "Please input your username!"
                          }
                        ]}
                        autoComplete="username"
                        required
                        className="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                        onChange={e => setUserName(e.target.value)}
                      />
                    </div>
                  </div>

                  <div className="space-y-1">
                    <label
                      htmlFor="password"
                      className="block text-sm font-medium text-gray-700"
                    >
                      Password
                    </label>
                    <div className="mt-1">
                      <input
                        id="password"
                        name="password"
                        type="password"
                        rules={[
                          {
                            required: true,
                            message : "Please input your password!"
                          }
                        ]}
                        autoComplete="current-password"
                        required
                        className="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                        onChange={e => setPassword(e.target.value)}
                      />
                    </div>
                  </div>

                  <div>
                    <button
                      type="submit"
                      onSubmit={handleSubmit}
                      className="flex w-full justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                    >
                      Sign in
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        <div className="relative hidden w-0 flex-1 lg:block">
          <img
            className="absolute inset-0 h-full w-full object-cover"
            src="https://www.ucalgary.ca/sites/default/files/styles/ucws_hero_cta_large_desktop/public/2022-05/21-ADV-188050-EmpoweringU-Digital_Experience3-8000x4500_1.jpg?itok=sOqhs9-j"
            alt=""
          />
        </div>
      </div>
    </>
  );
};

export default Login;
