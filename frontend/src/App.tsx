import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { QueryClient, QueryClientProvider } from "react-query"
import { Toaster } from "react-hot-toast"
import { AuthProvider } from "./contexts/AuthContext"
import { LanguageProvider } from "./contexts/LanguageContext"
import Navbar from "./components/Layout/Navbar"
import Footer from "./components/Layout/Footer"
import Home from "./pages/Home"
import Login from "./pages/Auth/Login"
import Register from "./pages/Auth/Register"
import Dashboard from "./pages/Dashboard"
import Content from "./pages/Content"
import ContentDetail from "./pages/ContentDetail"
import Modules from "./pages/Modules"
import ModuleDetail from "./pages/ModuleDetail"
import Quiz from "./pages/Quiz"
import LegalAid from "./pages/LegalAid"
import Profile from "./pages/Profile"
import Translation from "./pages/Translation"
import ProtectedRoute from "./components/Auth/ProtectedRoute"
import "./i18n"
import "./App.css"

const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <LanguageProvider>
          <Router>
            <div className="min-h-screen bg-gray-50 flex flex-col">
              <Navbar />
              <main className="flex-grow">
                <Routes>
                  <Route path="/" element={<Home />} />
                  <Route path="/login" element={<Login />} />
                  <Route path="/register" element={<Register />} />
                  <Route path="/content" element={<Content />} />
                  <Route path="/content/:id" element={<ContentDetail />} />
                  <Route path="/modules" element={<Modules />} />
                  <Route path="/modules/:id" element={<ModuleDetail />} />
                  <Route path="/legal-aid" element={<LegalAid />} />
                  <Route path="/translation" element={<Translation />} />
                  <Route
                    path="/dashboard"
                    element={
                      <ProtectedRoute>
                        <Dashboard />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/quiz"
                    element={
                      <ProtectedRoute>
                        <Quiz />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/profile"
                    element={
                      <ProtectedRoute>
                        <Profile />
                      </ProtectedRoute>
                    }
                  />
                </Routes>
              </main>
              <Footer />
              <Toaster position="top-right" />
            </div>
          </Router>
        </LanguageProvider>
      </AuthProvider>
    </QueryClientProvider>
  )
}

export default App
