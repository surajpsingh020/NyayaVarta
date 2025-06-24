import type React from "react"
import { Link } from "react-router-dom"
import { useTranslation } from "react-i18next"
import {
  BookOpenIcon,
  ScaleIcon,
  UserGroupIcon,
  LanguageIcon,
  MicrophoneIcon,
  AcademicCapIcon,
} from "@heroicons/react/24/outline"

const Home: React.FC = () => {
  const { t } = useTranslation()

  const features = [
    {
      icon: BookOpenIcon,
      title: t("home.features.content.title"),
      description: t("home.features.content.description"),
      link: "/content",
    },
    {
      icon: AcademicCapIcon,
      title: t("home.features.modules.title"),
      description: t("home.features.modules.description"),
      link: "/modules",
    },
    {
      icon: LanguageIcon,
      title: t("home.features.translation.title"),
      description: t("home.features.translation.description"),
      link: "/translation",
    },
    {
      icon: ScaleIcon,
      title: t("home.features.legalAid.title"),
      description: t("home.features.legalAid.description"),
      link: "/legal-aid",
    },
    {
      icon: MicrophoneIcon,
      title: t("home.features.voiceSupport.title"),
      description: t("home.features.voiceSupport.description"),
      link: "/translation",
    },
    {
      icon: UserGroupIcon,
      title: t("home.features.community.title"),
      description: t("home.features.community.description"),
      link: "/dashboard",
    },
  ]

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-blue-900 to-blue-700 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">{t("home.hero.title")}</h1>
            <p className="text-xl md:text-2xl mb-8 text-blue-100">{t("home.hero.subtitle")}</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                to="/content"
                className="bg-white text-blue-900 px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition duration-300"
              >
                {t("home.hero.exploreContent")}
              </Link>
              <Link
                to="/register"
                className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-blue-900 transition duration-300"
              >
                {t("home.hero.getStarted")}
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{t("home.features.title")}</h2>
            <p className="text-xl text-gray-600">{t("home.features.subtitle")}</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <Link
                key={index}
                to={feature.link}
                className="bg-gray-50 p-6 rounded-lg hover:shadow-lg transition duration-300 group"
              >
                <feature.icon className="h-12 w-12 text-blue-600 mb-4 group-hover:text-blue-700" />
                <h3 className="text-xl font-semibold text-gray-900 mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Statistics Section */}
      <section className="py-20 bg-blue-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{t("home.stats.title")}</h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div className="text-center">
              <div className="text-4xl font-bold text-blue-600 mb-2">10+</div>
              <div className="text-gray-600">{t("home.stats.languages")}</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-blue-600 mb-2">500+</div>
              <div className="text-gray-600">{t("home.stats.articles")}</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-blue-600 mb-2">50+</div>
              <div className="text-gray-600">{t("home.stats.modules")}</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-blue-600 mb-2">24/7</div>
              <div className="text-gray-600">{t("home.stats.support")}</div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gray-900 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">{t("home.cta.title")}</h2>
          <p className="text-xl mb-8 text-gray-300">{t("home.cta.subtitle")}</p>
          <Link
            to="/register"
            className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold transition duration-300"
          >
            {t("home.cta.button")}
          </Link>
        </div>
      </section>
    </div>
  )
}

export default Home
