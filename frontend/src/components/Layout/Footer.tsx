import type React from "react"
import { Link } from "react-router-dom"
import { useTranslation } from "react-i18next"
import { ScaleIcon } from "@heroicons/react/24/outline"

const Footer: React.FC = () => {
  const { t } = useTranslation()

  return (
    <footer className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-2 mb-4">
              <ScaleIcon className="h-8 w-8" />
              <span className="text-xl font-bold">NyayaVarta</span>
            </div>
            <p className="text-gray-300 mb-4">{t("footer.description")}</p>
            <p className="text-gray-400 text-sm">{t("footer.mission")}</p>
          </div>

          <div>
            <h3 className="text-lg font-semibold mb-4">{t("footer.quickLinks")}</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/content" className="text-gray-300 hover:text-white">
                  {t("nav.content")}
                </Link>
              </li>
              <li>
                <Link to="/modules" className="text-gray-300 hover:text-white">
                  {t("nav.modules")}
                </Link>
              </li>
              <li>
                <Link to="/legal-aid" className="text-gray-300 hover:text-white">
                  {t("nav.legalAid")}
                </Link>
              </li>
              <li>
                <Link to="/translation" className="text-gray-300 hover:text-white">
                  {t("nav.translation")}
                </Link>
              </li>
            </ul>
          </div>

          <div>
            <h3 className="text-lg font-semibold mb-4">{t("footer.support")}</h3>
            <ul className="space-y-2">
              <li>
                <a href="#" className="text-gray-300 hover:text-white">
                  {t("footer.helpCenter")}
                </a>
              </li>
              <li>
                <a href="#" className="text-gray-300 hover:text-white">
                  {t("footer.contactUs")}
                </a>
              </li>
              <li>
                <a href="#" className="text-gray-300 hover:text-white">
                  {t("footer.faq")}
                </a>
              </li>
              <li>
                <a href="#" className="text-gray-300 hover:text-white">
                  {t("footer.feedback")}
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-gray-700 mt-8 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-gray-400 text-sm">© 2024 NyayaVarta. {t("footer.allRightsReserved")}</p>
            <div className="flex space-x-6 mt-4 md:mt-0">
              <a href="#" className="text-gray-400 hover:text-white text-sm">
                {t("footer.privacy")}
              </a>
              <a href="#" className="text-gray-400 hover:text-white text-sm">
                {t("footer.terms")}
              </a>
              <a href="#" className="text-gray-400 hover:text-white text-sm">
                {t("footer.accessibility")}
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer
