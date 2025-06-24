"use client"

import type React from "react"
import { createContext, useContext, useState, useEffect, type ReactNode } from "react"
import axios from "axios"
import toast from "react-hot-toast"

interface User {
  id: number
  username: string
  email: string
  first_name: string
  last_name: string
  user_type: string
  preferred_language: string
  profile?: any
}

interface AuthContextType {
  user: User | null
  token: string | null
  login: (username: string, password: string) => Promise<boolean>
  register: (userData: any) => Promise<boolean>
  logout: () => void
  loading: boolean
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider")
  }
  return context
}

interface AuthProviderProps {
  children: ReactNode
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null)
  const [token, setToken] = useState<string | null>(localStorage.getItem("token"))
  const [loading, setLoading] = useState(true)

  const API_BASE_URL = process.env.REACT_APP_AUTH_SERVICE_URL || "http://localhost:8001"

  useEffect(() => {
    if (token) {
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`
      fetchUser()
    } else {
      setLoading(false)
    }
  }, [token])

  const fetchUser = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/profile/`)
      setUser(response.data)
    } catch (error) {
      console.error("Failed to fetch user:", error)
      logout()
    } finally {
      setLoading(false)
    }
  }

  const login = async (username: string, password: string): Promise<boolean> => {
    try {
      const response = await axios.post(`${API_BASE_URL}/api/login/`, {
        username,
        password,
      })

      const { user: userData, access } = response.data
      setUser(userData)
      setToken(access)
      localStorage.setItem("token", access)
      axios.defaults.headers.common["Authorization"] = `Bearer ${access}`

      toast.success("Login successful!")
      return true
    } catch (error: any) {
      toast.error(error.response?.data?.detail || "Login failed")
      return false
    }
  }

  const register = async (userData: any): Promise<boolean> => {
    try {
      const response = await axios.post(`${API_BASE_URL}/api/register/`, userData)

      const { user: newUser, access } = response.data
      setUser(newUser)
      setToken(access)
      localStorage.setItem("token", access)
      axios.defaults.headers.common["Authorization"] = `Bearer ${access}`

      toast.success("Registration successful!")
      return true
    } catch (error: any) {
      const errorMessage = error.response?.data?.detail || "Registration failed"
      toast.error(errorMessage)
      return false
    }
  }

  const logout = () => {
    setUser(null)
    setToken(null)
    localStorage.removeItem("token")
    delete axios.defaults.headers.common["Authorization"]
    toast.success("Logged out successfully")
  }

  const value = {
    user,
    token,
    login,
    register,
    logout,
    loading,
  }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}
