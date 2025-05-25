import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    close_button = (By.CLASS_NAME, 'close-button section-close')

    finish_order_button = (By.XPATH, "//button[@class='smart-button']")

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    sched_taxi_button = (By.CLASS_NAME, 'button round')
    comfort_tariff = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")

    phone_number_form = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.ID, 'phone')
    phone_number_next_button = (By.XPATH, "//button[@class='button full' and text()='Siguiente']")
    phone_code_field = (By.ID, 'code')
    phone_code_confirm_button = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")

    payment_method_button = (By.CLASS_NAME, 'pp-button filled')
    add_new_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_field = (By.XPATH, "//div[@class='card-number-input']/input[@id='number']")
    card_code_field = (By.XPATH, "//div[@class='card-code-input']/input[@id='code']")
    plc_lose_focus = (By.CLASS_NAME, 'plc')
    add_card_button = (By.XPATH, "//button[@class='button full' and text()='Agregar']")

    comment_field = (By.ID, 'comment')

    blanket_slider = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//input[@type='checkbox']")

    plus_ice_cream_button = (By.XPATH, "//div[@class='counter-plus' and text()='+']")
    ice_cream_counter = (By.CLASS_NAME, 'counter-value')

    order_details_popup = (By.CLASS_NAME, 'order-body')

    order_header_title = (By.CSS_SELECTOR, '.order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def click_close_button(self): #Boton de Cerrado de PopUps
        self.driver.find_element(*self.close_button).click()

    #Ingresar Direcciones
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def click_sched_taxi_button(self):
        self.driver.find_element(*self.sched_taxi_button).click()

    def click_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()

    def get_comfort_tariff_title(self):
        return self.driver.find_element(*self.comfort_tariff).get_property('title')

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    #Funcion Anexada con todos los pasos (Ruta y Tarifa)
    def set_route_and_comfort(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_sched_taxi_button()
        self.click_comfort_tariff()

    #Llenar numero de telefono y codigo
    def click_phone_number_form_button(self):
        self.driver.find_element(*self.phone_number_form).click()

    def fill_phone_number_field(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def click_next_phone_number_button (self):
        self.driver.find_element(*self.phone_number_next_button).click()

    def fill_phone_code_field(self, phone_code):
        self.driver.find_element(*self.phone_code_field).send_keys(phone_code)

    def get_phone_code(self):
        return self.driver.find_element(*self.phone_code_field).get_property('value')

    def click_confirm_phone_code_button(self):
        self.driver.find_element(*self.phone_code_confirm_button).click()

    #Funcion Anexada con todos los pasos (Telefono, codigo y agregarlo)
    def phone_number_and_code_full_function(self, phone_number, phone_code):
        self.click_phone_number_form_button()
        self.fill_phone_number_field(phone_number)
        self.click_next_phone_number_button()
        self.fill_phone_code_field(phone_code)
        self.click_confirm_phone_code_button()
        self.click_close_button()

    #Agregar Metodo de Pago Nuevo
    def click_payment_method_button(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_new_card_button(self):
        self.driver.find_element(*self.add_new_card_button).click()

    def fill_card_number_field(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def fill_card_code_number_field(self, card_code_number):
        self.driver.find_element(*self.card_code_field).send_keys(card_code_number)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_card_code_number(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def plc_lose_focus(self):
        self.driver.find_element(*self.plc_lose_focus).click()

    def is_add_card_button_enabled(self):
        return self.driver.find_element(*self.add_card_button).is_enabled()

    def click_add_card(self):
        self.driver.find_element(*self.add_card_button).click()

    #Funcion Anexada con todos los pasos para agregar una nueva tarjeta
    def add_payment_method_full(self, card_number, card_code_number):
        self.click_payment_method_button()
        self.click_add_new_card_button()
        self.fill_card_number_field(card_number)
        self.fill_card_code_number_field(card_code_number)
        self.plc_lose_focus()

        if self.is_add_card_button_enabled():
            self.click_add_card()
        else:
            raise Exception("El boton para agregar la tarjeta no esta habilitado, revise el proceso")
        self.click_close_button()

    #Enviar Mensaje al controlador pasos
    def fill_driver_message_field(self, comment_for_driver):
        self.driver.find_element(*self.comment_field).send_keys(comment_for_driver)

    def get_driver_message(self):
        return self.driver.find_element(*self.comment_field).get_property('value')

    #Pedir Manta y Pañuelos
    def click_blanket_slider(self):
        self.driver.find_element(*self.blanket_slider).click()

    def is_blanket_slider_enabled(self):
        return self.driver.find_element(*self.blanket_slider).is_enabled()

    #Pedir Helado
    def render_ice_cream_button(self):
        self.driver.find_element(*self.plus_ice_cream_button).scroll_into_view()

    def click_order_ice_cream(self):
        self.driver.find_element(*self.plus_ice_cream_button).click()

    def get_ice_cream_counter(self):
        return self.driver.find_element(*self.ice_cream_counter).get_property('value')

    #Pedir Taxi
    def click_finish_order_button(self):
        self.driver.find_element(*self.finish_order_button).click()

    def wait_for_order_details(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(*self.order_details_popup))
        return self.driver.find_element(*self.order_header_title).text

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        address_from = data.address_from
        address_to = data.address_to

        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == address_from, f'Expected to find "East 2nd Street, 601", but found {address_from}'
        assert routes_page.get_to() == address_to, f'Expected to find "1300 1st Street", but found {address_to}'

    def test_select_plan(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.click_comfort_tariff()

        assert routes_page.get_comfort_tariff_title() == 'Comfort' , f'Expected to find "Comfort" tariff selected, but found "{routes_page.getcomfort_tariff_title()}" instead'

    def test_fill_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        phone_number = data.phone_number
        phone_code = retrieve_phone_code(driver)

        routes_page.phone_number_and_code_full_function(phone_number, phone_code)

        assert routes_page.get_phone_number() == phone_number, f'Expected to find "+1 123 123 12 12", but found {phone_number}'
        assert routes_page.get_phone_code() == phone_code, f'Expected to find "phone code", but found {phone_code}'

    def test_fill_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        card_number = data.card_number
        card_code_number = data.card_code

        routes_page.add_payment_method_full(card_number, card_code_number)

        assert routes_page.get_card_number() == card_number, f'Expected to find "1234 5678 9100", but found {card_number}'
        assert routes_page.get_card_code_number() == card_code_number, f'Expected to find "111", but found {card_code_number}'

    def test_comment_for_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        comment_for_driver = data.message_for_driver

        routes_page.fill_driver_message_field(comment_for_driver)

        assert routes_page.get_driver_message() == comment_for_driver , f'Expected to find "driver message", but found {comment_for_driver}'

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.click_blanket_slider()

        assert routes_page.is_blanket_slider_enabled() == True , f'Expected to find blanket_slider selected, but found {routes_page.is_blanket_slider_enabled()}'

    def test_order_2_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.render_ice_cream_button()
        for i in range(2):
            routes_page.click_order_ice_cream()

        assert routes_page.get_ice_cream_counter() == 2 , f'Expected to find "2" in counter, but found {routes_page.get_ice_cream_counter}'

    def test_driver_info_appears(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.click_finish_order_button()
        order_title = routes_page.wait_for_order_details()

        assert "El conductor llegará en" in order_title , f'Expected "El conductor llegara en x min", but found "{order_title}'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        print("Test Finished!")
