import streamlit.report_thread as ReportThread
from streamlit.server.server import Server


class SessionState(object):
    def __init__(self, **kwargs):
        """A new SessionState object."""
        for key, val in kwargs.items():
            setattr(self, key, val)


def get(**kwargs):
    """Gets a SessionState object for the current session.
    Creates a new object if necessary.
    """
    ctx = ReportThread.get_report_ctx()

    this_session = None

    current_server = Server.get_current()
    if hasattr(current_server, '_session_infos'):
        # Streamlit < 0.56
        session_infos = Server.get_current()._session_infos.values()
    else:
        session_infos = Server.get_current()._session_info_by_id.values()

    for session_info in session_infos:
        s = session_info.session
        if (
            # Streamlit < 0.54.0
            (hasattr(s, '_main_dg') and s._main_dg == ctx.main_dg)
            or
            # Streamlit >= 0.54.0
            (not hasattr(s, '_main_dg') and s.enqueue == ctx.enqueue)
        ):
            this_session = s

    if this_session is None:
        raise RuntimeError(
            "Could not get your Streamlit Session object."
            'Are you doing something fancy with threads?')

    # Got the session object! Now let's attach some state into it.

    if not hasattr(this_session, '_custom_session_state'):
        this_session._custom_session_state = SessionState(**kwargs)

    return this_session._custom_session_state