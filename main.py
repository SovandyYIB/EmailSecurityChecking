from kivy.app import App
from kivy.lang import Builder
from api_handler import check_ipqs

Builder.load_file('SecurityCheckerApp.kv')


class SecurityCheckerApp(App):
    def check_security(self, input_text):
        """
        Handles the button press to check security.
        """
        result_label = self.root.ids.result

        if not input_text.strip():
            result_label.text = "[color=ff0000]Error: Input cannot be empty![/color]"
            return

        # Call the IPQS API
        result_label.text = "Checking security... Please wait."
        result_ipqs = check_ipqs(input_text)

        if "error" in result_ipqs:
            result_label.text = f"[color=ff0000]{result_ipqs['error']}[/color]"
        else:
            # Format the results into a detailed output
            result_details = self.format_results(result_ipqs)
            result_label.text = result_details

    def format_results(self, result):
        """
        Formats the result into a detailed, readable string.
        """
        formatted_result = "[b]Security Check Results:[/b]\n"
        for key, value in result.items():
            formatted_result += f"{key}: {value}\n"
        return formatted_result


if __name__ == "__main__":
    SecurityCheckerApp().run()
