import pytest
from fastapi import HTTPException

from app.beer_params.beer_params_dto import BeerParamInsertionDTO, BeerParamUpdateDTO
from app.beer_params.beer_params_service import get_beer_parameters, get_beer_param_per_name, update_beer_param, add_beer_param, delete_beer_param


class TestBeerParams:

    def test_get_beer_parameters(self, db_session):
        get_result = get_beer_parameters(db_session=db_session)
        assert len(get_result) != 0

    @pytest.mark.dependency()
    def test_get_beer_param_per_name(self, beer_name, db_session):
        get_result = get_beer_param_per_name(db_session=db_session, beer_name=beer_name)
        assert get_result.name == beer_name

    @pytest.mark.dependency(depends=['TestBeerParams::test_get_beer_param_per_name'])
    def test_get_properties(self, list_attributes_to_check, beer_name, db_session):
        get_result = get_beer_param_per_name(db_session=db_session, beer_name=beer_name)
        list_result_properties = dir(get_result)
        assert all(attribute in list_result_properties for attribute in list_attributes_to_check)

    @pytest.mark.dependency(depends=['TestBeerParams::test_get_beer_param_per_name'])
    def test_update_beer_param(self, beer_name, db_session):
        get_result = get_beer_param_per_name(db_session=db_session, beer_name=beer_name)
        test_update = BeerParamUpdateDTO()
        test_update.name = get_result.name
        for attr in BeerParamInsertionDTO.__dict__['__fields__'].keys():
            if attr != 'name':
                if type(getattr(get_result, attr)) == str:
                    setattr(test_update, attr, 'auto_testing')
                elif type(getattr(get_result, attr)) == float:
                    setattr(test_update, attr, 0.0001)
        _ = update_beer_param(beer_parameter=test_update, is_test=True, db_session=db_session)
        result_update = get_beer_param_per_name(db_session=db_session, beer_name=beer_name)
        for attr in result_update.__dict__.keys():
            if attr != 'name':
                if type(getattr(result_update, attr)) == str:
                    assert getattr(result_update, attr) == 'auto_testing'
                elif type(getattr(result_update, attr)) == float:
                    assert getattr(result_update, attr) == 0.0001

    @pytest.mark.dependency(depends=['TestBeerParams::test_get_beer_param_per_name'])
    def test_delete_beer_param(self, beer_name, db_session):
        result_delete = delete_beer_param(beer_name=beer_name, db_session=db_session, is_test=True)
        assert result_delete == 'Beer deleted with success !'

    @pytest.mark.dependency(depends=['TestBeerParams::test_get_beer_param_per_name'])
    def test_add_beer_param(self, beer_insertion, db_session):
        add_result = add_beer_param(beer_parameter=beer_insertion, db_session=db_session, is_test=True)
        assert add_result == 'Beer Parameter inserted with success !'
        get_result = get_beer_param_per_name(db_session=db_session, beer_name=beer_insertion.name)
        assert get_result.color == 'unknown'

    def test_fail_add_beer_param(self, fail_beer_insertion, db_session):
        try:
            _ = add_beer_param(beer_parameter=fail_beer_insertion, db_session=db_session, is_test=True)
            assert 0, 'Deliberate Fail as UNIQUE KEY constraint should block it!'
        except HTTPException as e:
            assert ('UNIQUE constraint failed: BeerParams.name' in e.detail)
